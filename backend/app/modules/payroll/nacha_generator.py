"""
NACHA Direct Deposit File & SEPA XML ISO 20022 Direct Credit Generator
Generates banking transmission files for multi-bank electronic payroll disbursement.
"""
from datetime import datetime, date
from typing import List, Dict, Any, Optional
import hashlib
import xml.etree.ElementTree as ET


class NACHAFileGenerator:
    """
    Constructs ACH compliant fixed-width 94-character records.
    Record Types:
      1: File Header Record
      5: Company / Batch Header Record
      6: Entry Detail Record (PPD - Prearranged Payment and Deposit)
      7: Addenda Record (Optional)
      8: Company / Batch Control Record
      9: File Control Record
    """
    @staticmethod
    def pad_left_zero(val: Any, length: int) -> str:
        s = str(val) if val is not None else "0"
        return s.zfill(length)[:length]

    @staticmethod
    def pad_right_space(val: Any, length: int) -> str:
        s = str(val) if val is not None else ""
        return (s + " " * length)[:length]

    @classmethod
    def generate_ach_file(
        cls,
        immediate_destination: str,  # 9-digit routing number with leading space or ' ' + 9 digits
        immediate_origin: str,       # Company EIN / Tax ID (10 chars, e.g. ' 123456789')
        company_name: str,
        company_id: str,
        effective_entry_date: date,
        employee_payments: List[Dict[str, Any]]
    ) -> str:
        now = datetime.now()
        date_str = now.strftime("%y%m%d")
        time_str = now.strftime("%H%M")
        file_id_mod = "A"

        records: List[str] = []

        # 1. File Header Record (Type 1)
        rec_1 = (
            "1"
            + "01"                                                # Priority code
            + cls.pad_right_space(immediate_destination, 10)       # Immediate destination
            + cls.pad_right_space(immediate_origin, 10)            # Immediate origin
            + date_str                                             # File creation date
            + time_str                                             # File creation time
            + file_id_mod                                          # File ID modifier
            + "094"                                                # Record size
            + "10"                                                 # Blocking factor
            + "1"                                                  # Format code
            + cls.pad_right_space(company_name, 23)                # Destination name
            + cls.pad_right_space("HR MANAGEMENT SYSTEM", 23)           # Origin name
            + "00000000"                                           # Reference code
        )
        records.append(rec_1)

        # 2. Batch Header Record (Type 5)
        batch_num = 1
        sec_code = "PPD"  # Payroll Direct Deposit
        company_desc = "PAYROLL   "
        eff_date_str = effective_entry_date.strftime("%y%m%d")

        rec_5 = (
            "5"
            + "200"                                                # Service class code (200: mixed debits/credits, 220: credits only)
            + cls.pad_right_space(company_name, 16)                # Company name
            + cls.pad_right_space("", 20)                          # Company discretionary data
            + cls.pad_right_space(company_id, 10)                  # Company identification
            + sec_code                                             # Standard Entry Class
            + company_desc                                         # Company entry description
            + date_str                                             # Company descriptive date
            + eff_date_str                                         # Effective entry date
            + "   "                                                # Settlement date (blank for ODFI)
            + "1"                                                  # Originator status code
            + cls.pad_left_zero(immediate_destination[-9:-1], 8)   # Originating DFI ID
            + cls.pad_left_zero(batch_num, 7)                      # Batch number
        )
        records.append(rec_5)

        # 3. Entry Detail Records (Type 6)
        total_credit_cents = 0
        entry_hash = 0
        trace_seq = 1

        for emp in employee_payments:
            routing = str(emp.get("routing_number", "011000015")).zfill(9)
            account = str(emp.get("account_number", "123456789"))
            amount = float(emp.get("amount", 0.0))
            emp_name = str(emp.get("employee_name", "Employee"))
            emp_id = str(emp.get("employee_code", "EMP001"))

            amount_cents = int(round(amount * 100))
            total_credit_cents += amount_cents
            entry_hash += int(routing[:8])

            rec_6 = (
                "6"
                + "22"                                             # Transaction code (22: Automated Deposit / Credit)
                + cls.pad_left_zero(routing[:8], 8)                # Receiving DFI routing
                + routing[8]                                       # Check digit
                + cls.pad_right_space(account, 17)                 # DFI account number
                + cls.pad_left_zero(amount_cents, 10)              # Amount in cents
                + cls.pad_right_space(emp_id, 15)                  # Individual identification
                + cls.pad_right_space(emp_name, 22)                # Individual name
                + "  "                                             # Discretionary data
                + "0"                                              # Addenda record indicator
                + cls.pad_left_zero(immediate_destination[-9:-1], 8) # Trace number prefix
                + cls.pad_left_zero(trace_seq, 7)                  # Trace number seq
            )
            records.append(rec_6)
            trace_seq += 1

        # 4. Batch Control Record (Type 8)
        hash_10 = cls.pad_left_zero(str(entry_hash)[-10:], 10)
        rec_8 = (
            "8"
            + "200"                                                # Service class code
            + cls.pad_left_zero(len(employee_payments), 6)         # Entry/Addenda count
            + hash_10                                              # Entry hash
            + cls.pad_left_zero(0, 12)                             # Total debit amount
            + cls.pad_left_zero(total_credit_cents, 12)            # Total credit amount
            + cls.pad_right_space(company_id, 10)                  # Company identification
            + cls.pad_right_space("", 19)                          # Message authentication code
            + cls.pad_right_space("", 6)                           # Reserved
            + cls.pad_left_zero(immediate_destination[-9:-1], 8)   # Originating DFI ID
            + cls.pad_left_zero(batch_num, 7)                      # Batch number
        )
        records.append(rec_8)

        # 5. File Control Record (Type 9)
        total_records = len(records) + 1
        block_count = (total_records + 9) // 10
        padding_needed = (block_count * 10) - total_records

        rec_9 = (
            "9"
            + cls.pad_left_zero(1, 6)                              # Batch count
            + cls.pad_left_zero(block_count, 6)                    # Block count
            + cls.pad_left_zero(len(employee_payments), 8)         # Total entry/addenda count
            + hash_10                                              # Entry hash
            + cls.pad_left_zero(0, 12)                             # Total debit amount
            + cls.pad_left_zero(total_credit_cents, 12)            # Total credit amount
            + cls.pad_right_space("", 39)                          # Reserved
        )
        records.append(rec_9)

        # Pad remaining lines with 9s to fill block factor 10
        for _ in range(padding_needed):
            records.append("9" * 94)

        return "\n".join(records)


class SEPAFileGenerator:
    """
    Generates ISO 20022 pain.001.001.03 Credit Transfer Initiation XML for Euro zone salaries.
    """
    @classmethod
    def generate_sepa_xml(
        cls,
        message_id: str,
        initiating_party_name: str,
        debtor_name: str,
        debtor_iban: str,
        debtor_bic: str,
        execution_date: date,
        employee_transfers: List[Dict[str, Any]]
    ) -> str:
        root = ET.Element("Document", {
            "xmlns": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.03",
            "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance"
        })
        cstmr = ET.SubElement(root, "CstmrCdtTrfInitn")

        # Group Header
        grp_hdr = ET.SubElement(cstmr, "GrpHdr")
        ET.SubElement(grp_hdr, "MsgId").text = message_id
        ET.SubElement(grp_hdr, "CreDtTm").text = datetime.now().isoformat()
        ET.SubElement(grp_hdr, "NbOfTxs").text = str(len(employee_transfers))
        total_val = sum(float(t.get("amount", 0.0)) for t in employee_transfers)
        ET.SubElement(grp_hdr, "CtrlSum").text = f"{total_val:.2f}"
        
        initg_pty = ET.SubElement(grp_hdr, "InitgPty")
        ET.SubElement(initg_pty, "Nm").text = initiating_party_name

        # Payment Information Block
        pmt_inf = ET.SubElement(cstmr, "PmtInf")
        ET.SubElement(pmt_inf, "PmtInfId").text = f"PMT-{message_id}"
        ET.SubElement(pmt_inf, "PmtMtd").text = "TRF"
        ET.SubElement(pmt_inf, "NbOfTxs").text = str(len(employee_transfers))
        ET.SubElement(pmt_inf, "CtrlSum").text = f"{total_val:.2f}"

        pmt_tp_inf = ET.SubElement(pmt_inf, "PmtTpInf")
        svc_lvl = ET.SubElement(pmt_tp_inf, "SvcLvl")
        ET.SubElement(svc_lvl, "Cd").text = "SEPA"

        ET.SubElement(pmt_inf, "ReqdExctnDt").text = execution_date.isoformat()

        dbtr = ET.SubElement(pmt_inf, "Dbtr")
        ET.SubElement(dbtr, "Nm").text = debtor_name

        dbtr_acct = ET.SubElement(pmt_inf, "DbtrAcct")
        id_el = ET.SubElement(dbtr_acct, "Id")
        ET.SubElement(id_el, "IBAN").text = debtor_iban

        dbtr_agt = ET.SubElement(pmt_inf, "DbtrAgt")
        fin_instn_id = ET.SubElement(dbtr_agt, "FinInstnId")
        ET.SubElement(fin_instn_id, "BIC").text = debtor_bic

        ET.SubElement(pmt_inf, "ChrgBr").text = "SLEV"

        # Transactions
        for tx in employee_transfers:
            tx_inf = ET.SubElement(pmt_inf, "CdtTrfTxInf")
            pmt_id = ET.SubElement(tx_inf, "PmtId")
            ET.SubElement(pmt_id, "EndToEndId").text = tx.get("reference_id", f"SAL-{datetime.now().strftime('%Y%m')}")

            amt = ET.SubElement(tx_inf, "Amt")
            instd_amt = ET.SubElement(amt, "InstdAmt", {"Ccy": "EUR"})
            instd_amt.text = f"{float(tx.get('amount', 0.0)):.2f}"

            cdtr = ET.SubElement(tx_inf, "Cdtr")
            ET.SubElement(cdtr, "Nm").text = tx.get("employee_name", "Employee")

            cdtr_acct = ET.SubElement(tx_inf, "CdtrAcct")
            cdtr_id = ET.SubElement(cdtr_acct, "Id")
            ET.SubElement(cdtr_id, "IBAN").text = tx.get("iban", "FR7630006000011234567890189")

            if "bic" in tx:
                cdtr_agt = ET.SubElement(tx_inf, "CdtrAgt")
                c_fin = ET.SubElement(cdtr_agt, "FinInstnId")
                ET.SubElement(c_fin, "BIC").text = tx["bic"]

            rmt_inf = ET.SubElement(tx_inf, "RmtInf")
            ET.SubElement(rmt_inf, "Ustrd").text = f"Salary {execution_date.strftime('%B %Y')}"

        return ET.tostring(root, encoding="utf-8", xml_declaration=True).decode("utf-8")
