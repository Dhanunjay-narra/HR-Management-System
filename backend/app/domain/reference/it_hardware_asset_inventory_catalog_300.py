"""
Enterprise IT Asset Management Master Hardware Catalog (300 Device Profiles)
Prescribes procurement benchmarks, depreciation curves, vendor support terms, and MDM compliance payloads.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class HardwareAssetProfile:
    asset_sku: str
    model_name: str
    category: str
    oem_vendor: str
    standard_cost_usd: float
    depreciation_schedule_months: int
    mdm_profile: str


MASTER_300_HARDWARE_CATALOG: Dict[str, HardwareAssetProfile] = {
    "SKU-HW-0001": HardwareAssetProfile(
        asset_sku="SKU-HW-0001",
        model_name="Enterprise Hardware Asset SKU-HW-0001 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0002": HardwareAssetProfile(
        asset_sku="SKU-HW-0002",
        model_name="Enterprise Hardware Asset SKU-HW-0002 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0003": HardwareAssetProfile(
        asset_sku="SKU-HW-0003",
        model_name="Enterprise Hardware Asset SKU-HW-0003 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0004": HardwareAssetProfile(
        asset_sku="SKU-HW-0004",
        model_name="Enterprise Hardware Asset SKU-HW-0004 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0005": HardwareAssetProfile(
        asset_sku="SKU-HW-0005",
        model_name="Enterprise Hardware Asset SKU-HW-0005 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0006": HardwareAssetProfile(
        asset_sku="SKU-HW-0006",
        model_name="Enterprise Hardware Asset SKU-HW-0006 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0007": HardwareAssetProfile(
        asset_sku="SKU-HW-0007",
        model_name="Enterprise Hardware Asset SKU-HW-0007 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0008": HardwareAssetProfile(
        asset_sku="SKU-HW-0008",
        model_name="Enterprise Hardware Asset SKU-HW-0008 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0009": HardwareAssetProfile(
        asset_sku="SKU-HW-0009",
        model_name="Enterprise Hardware Asset SKU-HW-0009 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0010": HardwareAssetProfile(
        asset_sku="SKU-HW-0010",
        model_name="Enterprise Hardware Asset SKU-HW-0010 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0011": HardwareAssetProfile(
        asset_sku="SKU-HW-0011",
        model_name="Enterprise Hardware Asset SKU-HW-0011 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0012": HardwareAssetProfile(
        asset_sku="SKU-HW-0012",
        model_name="Enterprise Hardware Asset SKU-HW-0012 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0013": HardwareAssetProfile(
        asset_sku="SKU-HW-0013",
        model_name="Enterprise Hardware Asset SKU-HW-0013 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0014": HardwareAssetProfile(
        asset_sku="SKU-HW-0014",
        model_name="Enterprise Hardware Asset SKU-HW-0014 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0015": HardwareAssetProfile(
        asset_sku="SKU-HW-0015",
        model_name="Enterprise Hardware Asset SKU-HW-0015 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0016": HardwareAssetProfile(
        asset_sku="SKU-HW-0016",
        model_name="Enterprise Hardware Asset SKU-HW-0016 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0017": HardwareAssetProfile(
        asset_sku="SKU-HW-0017",
        model_name="Enterprise Hardware Asset SKU-HW-0017 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0018": HardwareAssetProfile(
        asset_sku="SKU-HW-0018",
        model_name="Enterprise Hardware Asset SKU-HW-0018 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0019": HardwareAssetProfile(
        asset_sku="SKU-HW-0019",
        model_name="Enterprise Hardware Asset SKU-HW-0019 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0020": HardwareAssetProfile(
        asset_sku="SKU-HW-0020",
        model_name="Enterprise Hardware Asset SKU-HW-0020 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0021": HardwareAssetProfile(
        asset_sku="SKU-HW-0021",
        model_name="Enterprise Hardware Asset SKU-HW-0021 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0022": HardwareAssetProfile(
        asset_sku="SKU-HW-0022",
        model_name="Enterprise Hardware Asset SKU-HW-0022 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0023": HardwareAssetProfile(
        asset_sku="SKU-HW-0023",
        model_name="Enterprise Hardware Asset SKU-HW-0023 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0024": HardwareAssetProfile(
        asset_sku="SKU-HW-0024",
        model_name="Enterprise Hardware Asset SKU-HW-0024 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0025": HardwareAssetProfile(
        asset_sku="SKU-HW-0025",
        model_name="Enterprise Hardware Asset SKU-HW-0025 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0026": HardwareAssetProfile(
        asset_sku="SKU-HW-0026",
        model_name="Enterprise Hardware Asset SKU-HW-0026 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0027": HardwareAssetProfile(
        asset_sku="SKU-HW-0027",
        model_name="Enterprise Hardware Asset SKU-HW-0027 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0028": HardwareAssetProfile(
        asset_sku="SKU-HW-0028",
        model_name="Enterprise Hardware Asset SKU-HW-0028 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0029": HardwareAssetProfile(
        asset_sku="SKU-HW-0029",
        model_name="Enterprise Hardware Asset SKU-HW-0029 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0030": HardwareAssetProfile(
        asset_sku="SKU-HW-0030",
        model_name="Enterprise Hardware Asset SKU-HW-0030 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0031": HardwareAssetProfile(
        asset_sku="SKU-HW-0031",
        model_name="Enterprise Hardware Asset SKU-HW-0031 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0032": HardwareAssetProfile(
        asset_sku="SKU-HW-0032",
        model_name="Enterprise Hardware Asset SKU-HW-0032 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0033": HardwareAssetProfile(
        asset_sku="SKU-HW-0033",
        model_name="Enterprise Hardware Asset SKU-HW-0033 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0034": HardwareAssetProfile(
        asset_sku="SKU-HW-0034",
        model_name="Enterprise Hardware Asset SKU-HW-0034 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0035": HardwareAssetProfile(
        asset_sku="SKU-HW-0035",
        model_name="Enterprise Hardware Asset SKU-HW-0035 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0036": HardwareAssetProfile(
        asset_sku="SKU-HW-0036",
        model_name="Enterprise Hardware Asset SKU-HW-0036 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0037": HardwareAssetProfile(
        asset_sku="SKU-HW-0037",
        model_name="Enterprise Hardware Asset SKU-HW-0037 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0038": HardwareAssetProfile(
        asset_sku="SKU-HW-0038",
        model_name="Enterprise Hardware Asset SKU-HW-0038 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0039": HardwareAssetProfile(
        asset_sku="SKU-HW-0039",
        model_name="Enterprise Hardware Asset SKU-HW-0039 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0040": HardwareAssetProfile(
        asset_sku="SKU-HW-0040",
        model_name="Enterprise Hardware Asset SKU-HW-0040 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0041": HardwareAssetProfile(
        asset_sku="SKU-HW-0041",
        model_name="Enterprise Hardware Asset SKU-HW-0041 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0042": HardwareAssetProfile(
        asset_sku="SKU-HW-0042",
        model_name="Enterprise Hardware Asset SKU-HW-0042 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0043": HardwareAssetProfile(
        asset_sku="SKU-HW-0043",
        model_name="Enterprise Hardware Asset SKU-HW-0043 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0044": HardwareAssetProfile(
        asset_sku="SKU-HW-0044",
        model_name="Enterprise Hardware Asset SKU-HW-0044 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0045": HardwareAssetProfile(
        asset_sku="SKU-HW-0045",
        model_name="Enterprise Hardware Asset SKU-HW-0045 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0046": HardwareAssetProfile(
        asset_sku="SKU-HW-0046",
        model_name="Enterprise Hardware Asset SKU-HW-0046 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0047": HardwareAssetProfile(
        asset_sku="SKU-HW-0047",
        model_name="Enterprise Hardware Asset SKU-HW-0047 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0048": HardwareAssetProfile(
        asset_sku="SKU-HW-0048",
        model_name="Enterprise Hardware Asset SKU-HW-0048 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0049": HardwareAssetProfile(
        asset_sku="SKU-HW-0049",
        model_name="Enterprise Hardware Asset SKU-HW-0049 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0050": HardwareAssetProfile(
        asset_sku="SKU-HW-0050",
        model_name="Enterprise Hardware Asset SKU-HW-0050 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0051": HardwareAssetProfile(
        asset_sku="SKU-HW-0051",
        model_name="Enterprise Hardware Asset SKU-HW-0051 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0052": HardwareAssetProfile(
        asset_sku="SKU-HW-0052",
        model_name="Enterprise Hardware Asset SKU-HW-0052 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0053": HardwareAssetProfile(
        asset_sku="SKU-HW-0053",
        model_name="Enterprise Hardware Asset SKU-HW-0053 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0054": HardwareAssetProfile(
        asset_sku="SKU-HW-0054",
        model_name="Enterprise Hardware Asset SKU-HW-0054 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0055": HardwareAssetProfile(
        asset_sku="SKU-HW-0055",
        model_name="Enterprise Hardware Asset SKU-HW-0055 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0056": HardwareAssetProfile(
        asset_sku="SKU-HW-0056",
        model_name="Enterprise Hardware Asset SKU-HW-0056 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0057": HardwareAssetProfile(
        asset_sku="SKU-HW-0057",
        model_name="Enterprise Hardware Asset SKU-HW-0057 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0058": HardwareAssetProfile(
        asset_sku="SKU-HW-0058",
        model_name="Enterprise Hardware Asset SKU-HW-0058 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0059": HardwareAssetProfile(
        asset_sku="SKU-HW-0059",
        model_name="Enterprise Hardware Asset SKU-HW-0059 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0060": HardwareAssetProfile(
        asset_sku="SKU-HW-0060",
        model_name="Enterprise Hardware Asset SKU-HW-0060 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0061": HardwareAssetProfile(
        asset_sku="SKU-HW-0061",
        model_name="Enterprise Hardware Asset SKU-HW-0061 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0062": HardwareAssetProfile(
        asset_sku="SKU-HW-0062",
        model_name="Enterprise Hardware Asset SKU-HW-0062 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0063": HardwareAssetProfile(
        asset_sku="SKU-HW-0063",
        model_name="Enterprise Hardware Asset SKU-HW-0063 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0064": HardwareAssetProfile(
        asset_sku="SKU-HW-0064",
        model_name="Enterprise Hardware Asset SKU-HW-0064 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0065": HardwareAssetProfile(
        asset_sku="SKU-HW-0065",
        model_name="Enterprise Hardware Asset SKU-HW-0065 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0066": HardwareAssetProfile(
        asset_sku="SKU-HW-0066",
        model_name="Enterprise Hardware Asset SKU-HW-0066 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0067": HardwareAssetProfile(
        asset_sku="SKU-HW-0067",
        model_name="Enterprise Hardware Asset SKU-HW-0067 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0068": HardwareAssetProfile(
        asset_sku="SKU-HW-0068",
        model_name="Enterprise Hardware Asset SKU-HW-0068 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0069": HardwareAssetProfile(
        asset_sku="SKU-HW-0069",
        model_name="Enterprise Hardware Asset SKU-HW-0069 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0070": HardwareAssetProfile(
        asset_sku="SKU-HW-0070",
        model_name="Enterprise Hardware Asset SKU-HW-0070 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0071": HardwareAssetProfile(
        asset_sku="SKU-HW-0071",
        model_name="Enterprise Hardware Asset SKU-HW-0071 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0072": HardwareAssetProfile(
        asset_sku="SKU-HW-0072",
        model_name="Enterprise Hardware Asset SKU-HW-0072 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0073": HardwareAssetProfile(
        asset_sku="SKU-HW-0073",
        model_name="Enterprise Hardware Asset SKU-HW-0073 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0074": HardwareAssetProfile(
        asset_sku="SKU-HW-0074",
        model_name="Enterprise Hardware Asset SKU-HW-0074 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0075": HardwareAssetProfile(
        asset_sku="SKU-HW-0075",
        model_name="Enterprise Hardware Asset SKU-HW-0075 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0076": HardwareAssetProfile(
        asset_sku="SKU-HW-0076",
        model_name="Enterprise Hardware Asset SKU-HW-0076 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0077": HardwareAssetProfile(
        asset_sku="SKU-HW-0077",
        model_name="Enterprise Hardware Asset SKU-HW-0077 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0078": HardwareAssetProfile(
        asset_sku="SKU-HW-0078",
        model_name="Enterprise Hardware Asset SKU-HW-0078 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0079": HardwareAssetProfile(
        asset_sku="SKU-HW-0079",
        model_name="Enterprise Hardware Asset SKU-HW-0079 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0080": HardwareAssetProfile(
        asset_sku="SKU-HW-0080",
        model_name="Enterprise Hardware Asset SKU-HW-0080 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0081": HardwareAssetProfile(
        asset_sku="SKU-HW-0081",
        model_name="Enterprise Hardware Asset SKU-HW-0081 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0082": HardwareAssetProfile(
        asset_sku="SKU-HW-0082",
        model_name="Enterprise Hardware Asset SKU-HW-0082 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0083": HardwareAssetProfile(
        asset_sku="SKU-HW-0083",
        model_name="Enterprise Hardware Asset SKU-HW-0083 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0084": HardwareAssetProfile(
        asset_sku="SKU-HW-0084",
        model_name="Enterprise Hardware Asset SKU-HW-0084 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0085": HardwareAssetProfile(
        asset_sku="SKU-HW-0085",
        model_name="Enterprise Hardware Asset SKU-HW-0085 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0086": HardwareAssetProfile(
        asset_sku="SKU-HW-0086",
        model_name="Enterprise Hardware Asset SKU-HW-0086 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0087": HardwareAssetProfile(
        asset_sku="SKU-HW-0087",
        model_name="Enterprise Hardware Asset SKU-HW-0087 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0088": HardwareAssetProfile(
        asset_sku="SKU-HW-0088",
        model_name="Enterprise Hardware Asset SKU-HW-0088 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0089": HardwareAssetProfile(
        asset_sku="SKU-HW-0089",
        model_name="Enterprise Hardware Asset SKU-HW-0089 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0090": HardwareAssetProfile(
        asset_sku="SKU-HW-0090",
        model_name="Enterprise Hardware Asset SKU-HW-0090 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0091": HardwareAssetProfile(
        asset_sku="SKU-HW-0091",
        model_name="Enterprise Hardware Asset SKU-HW-0091 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0092": HardwareAssetProfile(
        asset_sku="SKU-HW-0092",
        model_name="Enterprise Hardware Asset SKU-HW-0092 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0093": HardwareAssetProfile(
        asset_sku="SKU-HW-0093",
        model_name="Enterprise Hardware Asset SKU-HW-0093 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0094": HardwareAssetProfile(
        asset_sku="SKU-HW-0094",
        model_name="Enterprise Hardware Asset SKU-HW-0094 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0095": HardwareAssetProfile(
        asset_sku="SKU-HW-0095",
        model_name="Enterprise Hardware Asset SKU-HW-0095 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0096": HardwareAssetProfile(
        asset_sku="SKU-HW-0096",
        model_name="Enterprise Hardware Asset SKU-HW-0096 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0097": HardwareAssetProfile(
        asset_sku="SKU-HW-0097",
        model_name="Enterprise Hardware Asset SKU-HW-0097 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0098": HardwareAssetProfile(
        asset_sku="SKU-HW-0098",
        model_name="Enterprise Hardware Asset SKU-HW-0098 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0099": HardwareAssetProfile(
        asset_sku="SKU-HW-0099",
        model_name="Enterprise Hardware Asset SKU-HW-0099 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0100": HardwareAssetProfile(
        asset_sku="SKU-HW-0100",
        model_name="Enterprise Hardware Asset SKU-HW-0100 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0101": HardwareAssetProfile(
        asset_sku="SKU-HW-0101",
        model_name="Enterprise Hardware Asset SKU-HW-0101 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0102": HardwareAssetProfile(
        asset_sku="SKU-HW-0102",
        model_name="Enterprise Hardware Asset SKU-HW-0102 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0103": HardwareAssetProfile(
        asset_sku="SKU-HW-0103",
        model_name="Enterprise Hardware Asset SKU-HW-0103 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0104": HardwareAssetProfile(
        asset_sku="SKU-HW-0104",
        model_name="Enterprise Hardware Asset SKU-HW-0104 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0105": HardwareAssetProfile(
        asset_sku="SKU-HW-0105",
        model_name="Enterprise Hardware Asset SKU-HW-0105 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0106": HardwareAssetProfile(
        asset_sku="SKU-HW-0106",
        model_name="Enterprise Hardware Asset SKU-HW-0106 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0107": HardwareAssetProfile(
        asset_sku="SKU-HW-0107",
        model_name="Enterprise Hardware Asset SKU-HW-0107 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0108": HardwareAssetProfile(
        asset_sku="SKU-HW-0108",
        model_name="Enterprise Hardware Asset SKU-HW-0108 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0109": HardwareAssetProfile(
        asset_sku="SKU-HW-0109",
        model_name="Enterprise Hardware Asset SKU-HW-0109 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0110": HardwareAssetProfile(
        asset_sku="SKU-HW-0110",
        model_name="Enterprise Hardware Asset SKU-HW-0110 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0111": HardwareAssetProfile(
        asset_sku="SKU-HW-0111",
        model_name="Enterprise Hardware Asset SKU-HW-0111 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0112": HardwareAssetProfile(
        asset_sku="SKU-HW-0112",
        model_name="Enterprise Hardware Asset SKU-HW-0112 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0113": HardwareAssetProfile(
        asset_sku="SKU-HW-0113",
        model_name="Enterprise Hardware Asset SKU-HW-0113 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0114": HardwareAssetProfile(
        asset_sku="SKU-HW-0114",
        model_name="Enterprise Hardware Asset SKU-HW-0114 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0115": HardwareAssetProfile(
        asset_sku="SKU-HW-0115",
        model_name="Enterprise Hardware Asset SKU-HW-0115 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0116": HardwareAssetProfile(
        asset_sku="SKU-HW-0116",
        model_name="Enterprise Hardware Asset SKU-HW-0116 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0117": HardwareAssetProfile(
        asset_sku="SKU-HW-0117",
        model_name="Enterprise Hardware Asset SKU-HW-0117 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0118": HardwareAssetProfile(
        asset_sku="SKU-HW-0118",
        model_name="Enterprise Hardware Asset SKU-HW-0118 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0119": HardwareAssetProfile(
        asset_sku="SKU-HW-0119",
        model_name="Enterprise Hardware Asset SKU-HW-0119 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0120": HardwareAssetProfile(
        asset_sku="SKU-HW-0120",
        model_name="Enterprise Hardware Asset SKU-HW-0120 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0121": HardwareAssetProfile(
        asset_sku="SKU-HW-0121",
        model_name="Enterprise Hardware Asset SKU-HW-0121 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0122": HardwareAssetProfile(
        asset_sku="SKU-HW-0122",
        model_name="Enterprise Hardware Asset SKU-HW-0122 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0123": HardwareAssetProfile(
        asset_sku="SKU-HW-0123",
        model_name="Enterprise Hardware Asset SKU-HW-0123 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0124": HardwareAssetProfile(
        asset_sku="SKU-HW-0124",
        model_name="Enterprise Hardware Asset SKU-HW-0124 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0125": HardwareAssetProfile(
        asset_sku="SKU-HW-0125",
        model_name="Enterprise Hardware Asset SKU-HW-0125 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0126": HardwareAssetProfile(
        asset_sku="SKU-HW-0126",
        model_name="Enterprise Hardware Asset SKU-HW-0126 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0127": HardwareAssetProfile(
        asset_sku="SKU-HW-0127",
        model_name="Enterprise Hardware Asset SKU-HW-0127 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0128": HardwareAssetProfile(
        asset_sku="SKU-HW-0128",
        model_name="Enterprise Hardware Asset SKU-HW-0128 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0129": HardwareAssetProfile(
        asset_sku="SKU-HW-0129",
        model_name="Enterprise Hardware Asset SKU-HW-0129 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0130": HardwareAssetProfile(
        asset_sku="SKU-HW-0130",
        model_name="Enterprise Hardware Asset SKU-HW-0130 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0131": HardwareAssetProfile(
        asset_sku="SKU-HW-0131",
        model_name="Enterprise Hardware Asset SKU-HW-0131 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0132": HardwareAssetProfile(
        asset_sku="SKU-HW-0132",
        model_name="Enterprise Hardware Asset SKU-HW-0132 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0133": HardwareAssetProfile(
        asset_sku="SKU-HW-0133",
        model_name="Enterprise Hardware Asset SKU-HW-0133 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0134": HardwareAssetProfile(
        asset_sku="SKU-HW-0134",
        model_name="Enterprise Hardware Asset SKU-HW-0134 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0135": HardwareAssetProfile(
        asset_sku="SKU-HW-0135",
        model_name="Enterprise Hardware Asset SKU-HW-0135 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0136": HardwareAssetProfile(
        asset_sku="SKU-HW-0136",
        model_name="Enterprise Hardware Asset SKU-HW-0136 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0137": HardwareAssetProfile(
        asset_sku="SKU-HW-0137",
        model_name="Enterprise Hardware Asset SKU-HW-0137 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0138": HardwareAssetProfile(
        asset_sku="SKU-HW-0138",
        model_name="Enterprise Hardware Asset SKU-HW-0138 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0139": HardwareAssetProfile(
        asset_sku="SKU-HW-0139",
        model_name="Enterprise Hardware Asset SKU-HW-0139 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0140": HardwareAssetProfile(
        asset_sku="SKU-HW-0140",
        model_name="Enterprise Hardware Asset SKU-HW-0140 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0141": HardwareAssetProfile(
        asset_sku="SKU-HW-0141",
        model_name="Enterprise Hardware Asset SKU-HW-0141 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0142": HardwareAssetProfile(
        asset_sku="SKU-HW-0142",
        model_name="Enterprise Hardware Asset SKU-HW-0142 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0143": HardwareAssetProfile(
        asset_sku="SKU-HW-0143",
        model_name="Enterprise Hardware Asset SKU-HW-0143 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0144": HardwareAssetProfile(
        asset_sku="SKU-HW-0144",
        model_name="Enterprise Hardware Asset SKU-HW-0144 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0145": HardwareAssetProfile(
        asset_sku="SKU-HW-0145",
        model_name="Enterprise Hardware Asset SKU-HW-0145 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0146": HardwareAssetProfile(
        asset_sku="SKU-HW-0146",
        model_name="Enterprise Hardware Asset SKU-HW-0146 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0147": HardwareAssetProfile(
        asset_sku="SKU-HW-0147",
        model_name="Enterprise Hardware Asset SKU-HW-0147 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0148": HardwareAssetProfile(
        asset_sku="SKU-HW-0148",
        model_name="Enterprise Hardware Asset SKU-HW-0148 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0149": HardwareAssetProfile(
        asset_sku="SKU-HW-0149",
        model_name="Enterprise Hardware Asset SKU-HW-0149 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0150": HardwareAssetProfile(
        asset_sku="SKU-HW-0150",
        model_name="Enterprise Hardware Asset SKU-HW-0150 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0151": HardwareAssetProfile(
        asset_sku="SKU-HW-0151",
        model_name="Enterprise Hardware Asset SKU-HW-0151 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0152": HardwareAssetProfile(
        asset_sku="SKU-HW-0152",
        model_name="Enterprise Hardware Asset SKU-HW-0152 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0153": HardwareAssetProfile(
        asset_sku="SKU-HW-0153",
        model_name="Enterprise Hardware Asset SKU-HW-0153 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0154": HardwareAssetProfile(
        asset_sku="SKU-HW-0154",
        model_name="Enterprise Hardware Asset SKU-HW-0154 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0155": HardwareAssetProfile(
        asset_sku="SKU-HW-0155",
        model_name="Enterprise Hardware Asset SKU-HW-0155 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0156": HardwareAssetProfile(
        asset_sku="SKU-HW-0156",
        model_name="Enterprise Hardware Asset SKU-HW-0156 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0157": HardwareAssetProfile(
        asset_sku="SKU-HW-0157",
        model_name="Enterprise Hardware Asset SKU-HW-0157 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0158": HardwareAssetProfile(
        asset_sku="SKU-HW-0158",
        model_name="Enterprise Hardware Asset SKU-HW-0158 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0159": HardwareAssetProfile(
        asset_sku="SKU-HW-0159",
        model_name="Enterprise Hardware Asset SKU-HW-0159 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0160": HardwareAssetProfile(
        asset_sku="SKU-HW-0160",
        model_name="Enterprise Hardware Asset SKU-HW-0160 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0161": HardwareAssetProfile(
        asset_sku="SKU-HW-0161",
        model_name="Enterprise Hardware Asset SKU-HW-0161 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0162": HardwareAssetProfile(
        asset_sku="SKU-HW-0162",
        model_name="Enterprise Hardware Asset SKU-HW-0162 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0163": HardwareAssetProfile(
        asset_sku="SKU-HW-0163",
        model_name="Enterprise Hardware Asset SKU-HW-0163 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0164": HardwareAssetProfile(
        asset_sku="SKU-HW-0164",
        model_name="Enterprise Hardware Asset SKU-HW-0164 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0165": HardwareAssetProfile(
        asset_sku="SKU-HW-0165",
        model_name="Enterprise Hardware Asset SKU-HW-0165 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0166": HardwareAssetProfile(
        asset_sku="SKU-HW-0166",
        model_name="Enterprise Hardware Asset SKU-HW-0166 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0167": HardwareAssetProfile(
        asset_sku="SKU-HW-0167",
        model_name="Enterprise Hardware Asset SKU-HW-0167 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0168": HardwareAssetProfile(
        asset_sku="SKU-HW-0168",
        model_name="Enterprise Hardware Asset SKU-HW-0168 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0169": HardwareAssetProfile(
        asset_sku="SKU-HW-0169",
        model_name="Enterprise Hardware Asset SKU-HW-0169 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0170": HardwareAssetProfile(
        asset_sku="SKU-HW-0170",
        model_name="Enterprise Hardware Asset SKU-HW-0170 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0171": HardwareAssetProfile(
        asset_sku="SKU-HW-0171",
        model_name="Enterprise Hardware Asset SKU-HW-0171 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0172": HardwareAssetProfile(
        asset_sku="SKU-HW-0172",
        model_name="Enterprise Hardware Asset SKU-HW-0172 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0173": HardwareAssetProfile(
        asset_sku="SKU-HW-0173",
        model_name="Enterprise Hardware Asset SKU-HW-0173 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0174": HardwareAssetProfile(
        asset_sku="SKU-HW-0174",
        model_name="Enterprise Hardware Asset SKU-HW-0174 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0175": HardwareAssetProfile(
        asset_sku="SKU-HW-0175",
        model_name="Enterprise Hardware Asset SKU-HW-0175 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0176": HardwareAssetProfile(
        asset_sku="SKU-HW-0176",
        model_name="Enterprise Hardware Asset SKU-HW-0176 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0177": HardwareAssetProfile(
        asset_sku="SKU-HW-0177",
        model_name="Enterprise Hardware Asset SKU-HW-0177 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0178": HardwareAssetProfile(
        asset_sku="SKU-HW-0178",
        model_name="Enterprise Hardware Asset SKU-HW-0178 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0179": HardwareAssetProfile(
        asset_sku="SKU-HW-0179",
        model_name="Enterprise Hardware Asset SKU-HW-0179 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0180": HardwareAssetProfile(
        asset_sku="SKU-HW-0180",
        model_name="Enterprise Hardware Asset SKU-HW-0180 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0181": HardwareAssetProfile(
        asset_sku="SKU-HW-0181",
        model_name="Enterprise Hardware Asset SKU-HW-0181 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0182": HardwareAssetProfile(
        asset_sku="SKU-HW-0182",
        model_name="Enterprise Hardware Asset SKU-HW-0182 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0183": HardwareAssetProfile(
        asset_sku="SKU-HW-0183",
        model_name="Enterprise Hardware Asset SKU-HW-0183 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0184": HardwareAssetProfile(
        asset_sku="SKU-HW-0184",
        model_name="Enterprise Hardware Asset SKU-HW-0184 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0185": HardwareAssetProfile(
        asset_sku="SKU-HW-0185",
        model_name="Enterprise Hardware Asset SKU-HW-0185 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0186": HardwareAssetProfile(
        asset_sku="SKU-HW-0186",
        model_name="Enterprise Hardware Asset SKU-HW-0186 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0187": HardwareAssetProfile(
        asset_sku="SKU-HW-0187",
        model_name="Enterprise Hardware Asset SKU-HW-0187 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0188": HardwareAssetProfile(
        asset_sku="SKU-HW-0188",
        model_name="Enterprise Hardware Asset SKU-HW-0188 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0189": HardwareAssetProfile(
        asset_sku="SKU-HW-0189",
        model_name="Enterprise Hardware Asset SKU-HW-0189 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0190": HardwareAssetProfile(
        asset_sku="SKU-HW-0190",
        model_name="Enterprise Hardware Asset SKU-HW-0190 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0191": HardwareAssetProfile(
        asset_sku="SKU-HW-0191",
        model_name="Enterprise Hardware Asset SKU-HW-0191 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0192": HardwareAssetProfile(
        asset_sku="SKU-HW-0192",
        model_name="Enterprise Hardware Asset SKU-HW-0192 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0193": HardwareAssetProfile(
        asset_sku="SKU-HW-0193",
        model_name="Enterprise Hardware Asset SKU-HW-0193 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0194": HardwareAssetProfile(
        asset_sku="SKU-HW-0194",
        model_name="Enterprise Hardware Asset SKU-HW-0194 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0195": HardwareAssetProfile(
        asset_sku="SKU-HW-0195",
        model_name="Enterprise Hardware Asset SKU-HW-0195 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0196": HardwareAssetProfile(
        asset_sku="SKU-HW-0196",
        model_name="Enterprise Hardware Asset SKU-HW-0196 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0197": HardwareAssetProfile(
        asset_sku="SKU-HW-0197",
        model_name="Enterprise Hardware Asset SKU-HW-0197 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0198": HardwareAssetProfile(
        asset_sku="SKU-HW-0198",
        model_name="Enterprise Hardware Asset SKU-HW-0198 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0199": HardwareAssetProfile(
        asset_sku="SKU-HW-0199",
        model_name="Enterprise Hardware Asset SKU-HW-0199 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0200": HardwareAssetProfile(
        asset_sku="SKU-HW-0200",
        model_name="Enterprise Hardware Asset SKU-HW-0200 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0201": HardwareAssetProfile(
        asset_sku="SKU-HW-0201",
        model_name="Enterprise Hardware Asset SKU-HW-0201 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0202": HardwareAssetProfile(
        asset_sku="SKU-HW-0202",
        model_name="Enterprise Hardware Asset SKU-HW-0202 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0203": HardwareAssetProfile(
        asset_sku="SKU-HW-0203",
        model_name="Enterprise Hardware Asset SKU-HW-0203 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0204": HardwareAssetProfile(
        asset_sku="SKU-HW-0204",
        model_name="Enterprise Hardware Asset SKU-HW-0204 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0205": HardwareAssetProfile(
        asset_sku="SKU-HW-0205",
        model_name="Enterprise Hardware Asset SKU-HW-0205 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0206": HardwareAssetProfile(
        asset_sku="SKU-HW-0206",
        model_name="Enterprise Hardware Asset SKU-HW-0206 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0207": HardwareAssetProfile(
        asset_sku="SKU-HW-0207",
        model_name="Enterprise Hardware Asset SKU-HW-0207 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0208": HardwareAssetProfile(
        asset_sku="SKU-HW-0208",
        model_name="Enterprise Hardware Asset SKU-HW-0208 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0209": HardwareAssetProfile(
        asset_sku="SKU-HW-0209",
        model_name="Enterprise Hardware Asset SKU-HW-0209 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0210": HardwareAssetProfile(
        asset_sku="SKU-HW-0210",
        model_name="Enterprise Hardware Asset SKU-HW-0210 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0211": HardwareAssetProfile(
        asset_sku="SKU-HW-0211",
        model_name="Enterprise Hardware Asset SKU-HW-0211 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0212": HardwareAssetProfile(
        asset_sku="SKU-HW-0212",
        model_name="Enterprise Hardware Asset SKU-HW-0212 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0213": HardwareAssetProfile(
        asset_sku="SKU-HW-0213",
        model_name="Enterprise Hardware Asset SKU-HW-0213 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0214": HardwareAssetProfile(
        asset_sku="SKU-HW-0214",
        model_name="Enterprise Hardware Asset SKU-HW-0214 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0215": HardwareAssetProfile(
        asset_sku="SKU-HW-0215",
        model_name="Enterprise Hardware Asset SKU-HW-0215 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0216": HardwareAssetProfile(
        asset_sku="SKU-HW-0216",
        model_name="Enterprise Hardware Asset SKU-HW-0216 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0217": HardwareAssetProfile(
        asset_sku="SKU-HW-0217",
        model_name="Enterprise Hardware Asset SKU-HW-0217 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0218": HardwareAssetProfile(
        asset_sku="SKU-HW-0218",
        model_name="Enterprise Hardware Asset SKU-HW-0218 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0219": HardwareAssetProfile(
        asset_sku="SKU-HW-0219",
        model_name="Enterprise Hardware Asset SKU-HW-0219 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0220": HardwareAssetProfile(
        asset_sku="SKU-HW-0220",
        model_name="Enterprise Hardware Asset SKU-HW-0220 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0221": HardwareAssetProfile(
        asset_sku="SKU-HW-0221",
        model_name="Enterprise Hardware Asset SKU-HW-0221 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0222": HardwareAssetProfile(
        asset_sku="SKU-HW-0222",
        model_name="Enterprise Hardware Asset SKU-HW-0222 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0223": HardwareAssetProfile(
        asset_sku="SKU-HW-0223",
        model_name="Enterprise Hardware Asset SKU-HW-0223 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0224": HardwareAssetProfile(
        asset_sku="SKU-HW-0224",
        model_name="Enterprise Hardware Asset SKU-HW-0224 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0225": HardwareAssetProfile(
        asset_sku="SKU-HW-0225",
        model_name="Enterprise Hardware Asset SKU-HW-0225 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0226": HardwareAssetProfile(
        asset_sku="SKU-HW-0226",
        model_name="Enterprise Hardware Asset SKU-HW-0226 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0227": HardwareAssetProfile(
        asset_sku="SKU-HW-0227",
        model_name="Enterprise Hardware Asset SKU-HW-0227 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0228": HardwareAssetProfile(
        asset_sku="SKU-HW-0228",
        model_name="Enterprise Hardware Asset SKU-HW-0228 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0229": HardwareAssetProfile(
        asset_sku="SKU-HW-0229",
        model_name="Enterprise Hardware Asset SKU-HW-0229 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0230": HardwareAssetProfile(
        asset_sku="SKU-HW-0230",
        model_name="Enterprise Hardware Asset SKU-HW-0230 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0231": HardwareAssetProfile(
        asset_sku="SKU-HW-0231",
        model_name="Enterprise Hardware Asset SKU-HW-0231 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0232": HardwareAssetProfile(
        asset_sku="SKU-HW-0232",
        model_name="Enterprise Hardware Asset SKU-HW-0232 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0233": HardwareAssetProfile(
        asset_sku="SKU-HW-0233",
        model_name="Enterprise Hardware Asset SKU-HW-0233 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0234": HardwareAssetProfile(
        asset_sku="SKU-HW-0234",
        model_name="Enterprise Hardware Asset SKU-HW-0234 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0235": HardwareAssetProfile(
        asset_sku="SKU-HW-0235",
        model_name="Enterprise Hardware Asset SKU-HW-0235 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0236": HardwareAssetProfile(
        asset_sku="SKU-HW-0236",
        model_name="Enterprise Hardware Asset SKU-HW-0236 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0237": HardwareAssetProfile(
        asset_sku="SKU-HW-0237",
        model_name="Enterprise Hardware Asset SKU-HW-0237 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0238": HardwareAssetProfile(
        asset_sku="SKU-HW-0238",
        model_name="Enterprise Hardware Asset SKU-HW-0238 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0239": HardwareAssetProfile(
        asset_sku="SKU-HW-0239",
        model_name="Enterprise Hardware Asset SKU-HW-0239 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0240": HardwareAssetProfile(
        asset_sku="SKU-HW-0240",
        model_name="Enterprise Hardware Asset SKU-HW-0240 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0241": HardwareAssetProfile(
        asset_sku="SKU-HW-0241",
        model_name="Enterprise Hardware Asset SKU-HW-0241 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0242": HardwareAssetProfile(
        asset_sku="SKU-HW-0242",
        model_name="Enterprise Hardware Asset SKU-HW-0242 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0243": HardwareAssetProfile(
        asset_sku="SKU-HW-0243",
        model_name="Enterprise Hardware Asset SKU-HW-0243 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0244": HardwareAssetProfile(
        asset_sku="SKU-HW-0244",
        model_name="Enterprise Hardware Asset SKU-HW-0244 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0245": HardwareAssetProfile(
        asset_sku="SKU-HW-0245",
        model_name="Enterprise Hardware Asset SKU-HW-0245 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0246": HardwareAssetProfile(
        asset_sku="SKU-HW-0246",
        model_name="Enterprise Hardware Asset SKU-HW-0246 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0247": HardwareAssetProfile(
        asset_sku="SKU-HW-0247",
        model_name="Enterprise Hardware Asset SKU-HW-0247 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0248": HardwareAssetProfile(
        asset_sku="SKU-HW-0248",
        model_name="Enterprise Hardware Asset SKU-HW-0248 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0249": HardwareAssetProfile(
        asset_sku="SKU-HW-0249",
        model_name="Enterprise Hardware Asset SKU-HW-0249 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0250": HardwareAssetProfile(
        asset_sku="SKU-HW-0250",
        model_name="Enterprise Hardware Asset SKU-HW-0250 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0251": HardwareAssetProfile(
        asset_sku="SKU-HW-0251",
        model_name="Enterprise Hardware Asset SKU-HW-0251 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0252": HardwareAssetProfile(
        asset_sku="SKU-HW-0252",
        model_name="Enterprise Hardware Asset SKU-HW-0252 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0253": HardwareAssetProfile(
        asset_sku="SKU-HW-0253",
        model_name="Enterprise Hardware Asset SKU-HW-0253 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0254": HardwareAssetProfile(
        asset_sku="SKU-HW-0254",
        model_name="Enterprise Hardware Asset SKU-HW-0254 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0255": HardwareAssetProfile(
        asset_sku="SKU-HW-0255",
        model_name="Enterprise Hardware Asset SKU-HW-0255 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0256": HardwareAssetProfile(
        asset_sku="SKU-HW-0256",
        model_name="Enterprise Hardware Asset SKU-HW-0256 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0257": HardwareAssetProfile(
        asset_sku="SKU-HW-0257",
        model_name="Enterprise Hardware Asset SKU-HW-0257 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0258": HardwareAssetProfile(
        asset_sku="SKU-HW-0258",
        model_name="Enterprise Hardware Asset SKU-HW-0258 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0259": HardwareAssetProfile(
        asset_sku="SKU-HW-0259",
        model_name="Enterprise Hardware Asset SKU-HW-0259 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0260": HardwareAssetProfile(
        asset_sku="SKU-HW-0260",
        model_name="Enterprise Hardware Asset SKU-HW-0260 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0261": HardwareAssetProfile(
        asset_sku="SKU-HW-0261",
        model_name="Enterprise Hardware Asset SKU-HW-0261 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0262": HardwareAssetProfile(
        asset_sku="SKU-HW-0262",
        model_name="Enterprise Hardware Asset SKU-HW-0262 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0263": HardwareAssetProfile(
        asset_sku="SKU-HW-0263",
        model_name="Enterprise Hardware Asset SKU-HW-0263 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0264": HardwareAssetProfile(
        asset_sku="SKU-HW-0264",
        model_name="Enterprise Hardware Asset SKU-HW-0264 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0265": HardwareAssetProfile(
        asset_sku="SKU-HW-0265",
        model_name="Enterprise Hardware Asset SKU-HW-0265 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0266": HardwareAssetProfile(
        asset_sku="SKU-HW-0266",
        model_name="Enterprise Hardware Asset SKU-HW-0266 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0267": HardwareAssetProfile(
        asset_sku="SKU-HW-0267",
        model_name="Enterprise Hardware Asset SKU-HW-0267 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0268": HardwareAssetProfile(
        asset_sku="SKU-HW-0268",
        model_name="Enterprise Hardware Asset SKU-HW-0268 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0269": HardwareAssetProfile(
        asset_sku="SKU-HW-0269",
        model_name="Enterprise Hardware Asset SKU-HW-0269 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0270": HardwareAssetProfile(
        asset_sku="SKU-HW-0270",
        model_name="Enterprise Hardware Asset SKU-HW-0270 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0271": HardwareAssetProfile(
        asset_sku="SKU-HW-0271",
        model_name="Enterprise Hardware Asset SKU-HW-0271 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0272": HardwareAssetProfile(
        asset_sku="SKU-HW-0272",
        model_name="Enterprise Hardware Asset SKU-HW-0272 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0273": HardwareAssetProfile(
        asset_sku="SKU-HW-0273",
        model_name="Enterprise Hardware Asset SKU-HW-0273 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0274": HardwareAssetProfile(
        asset_sku="SKU-HW-0274",
        model_name="Enterprise Hardware Asset SKU-HW-0274 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0275": HardwareAssetProfile(
        asset_sku="SKU-HW-0275",
        model_name="Enterprise Hardware Asset SKU-HW-0275 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0276": HardwareAssetProfile(
        asset_sku="SKU-HW-0276",
        model_name="Enterprise Hardware Asset SKU-HW-0276 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0277": HardwareAssetProfile(
        asset_sku="SKU-HW-0277",
        model_name="Enterprise Hardware Asset SKU-HW-0277 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0278": HardwareAssetProfile(
        asset_sku="SKU-HW-0278",
        model_name="Enterprise Hardware Asset SKU-HW-0278 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0279": HardwareAssetProfile(
        asset_sku="SKU-HW-0279",
        model_name="Enterprise Hardware Asset SKU-HW-0279 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0280": HardwareAssetProfile(
        asset_sku="SKU-HW-0280",
        model_name="Enterprise Hardware Asset SKU-HW-0280 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0281": HardwareAssetProfile(
        asset_sku="SKU-HW-0281",
        model_name="Enterprise Hardware Asset SKU-HW-0281 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0282": HardwareAssetProfile(
        asset_sku="SKU-HW-0282",
        model_name="Enterprise Hardware Asset SKU-HW-0282 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0283": HardwareAssetProfile(
        asset_sku="SKU-HW-0283",
        model_name="Enterprise Hardware Asset SKU-HW-0283 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0284": HardwareAssetProfile(
        asset_sku="SKU-HW-0284",
        model_name="Enterprise Hardware Asset SKU-HW-0284 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0285": HardwareAssetProfile(
        asset_sku="SKU-HW-0285",
        model_name="Enterprise Hardware Asset SKU-HW-0285 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0286": HardwareAssetProfile(
        asset_sku="SKU-HW-0286",
        model_name="Enterprise Hardware Asset SKU-HW-0286 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0287": HardwareAssetProfile(
        asset_sku="SKU-HW-0287",
        model_name="Enterprise Hardware Asset SKU-HW-0287 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0288": HardwareAssetProfile(
        asset_sku="SKU-HW-0288",
        model_name="Enterprise Hardware Asset SKU-HW-0288 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0289": HardwareAssetProfile(
        asset_sku="SKU-HW-0289",
        model_name="Enterprise Hardware Asset SKU-HW-0289 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0290": HardwareAssetProfile(
        asset_sku="SKU-HW-0290",
        model_name="Enterprise Hardware Asset SKU-HW-0290 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0291": HardwareAssetProfile(
        asset_sku="SKU-HW-0291",
        model_name="Enterprise Hardware Asset SKU-HW-0291 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2450.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0292": HardwareAssetProfile(
        asset_sku="SKU-HW-0292",
        model_name="Enterprise Hardware Asset SKU-HW-0292 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1050.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0293": HardwareAssetProfile(
        asset_sku="SKU-HW-0293",
        model_name="Enterprise Hardware Asset SKU-HW-0293 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=205.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0294": HardwareAssetProfile(
        asset_sku="SKU-HW-0294",
        model_name="Enterprise Hardware Asset SKU-HW-0294 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=550.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0295": HardwareAssetProfile(
        asset_sku="SKU-HW-0295",
        model_name="Enterprise Hardware Asset SKU-HW-0295 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4750.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
    "SKU-HW-0296": HardwareAssetProfile(
        asset_sku="SKU-HW-0296",
        model_name="Enterprise Hardware Asset SKU-HW-0296 (Laptops & Mobile Workstations)",
        category="Laptops & Mobile Workstations",
        oem_vendor="Apple / Dell / Lenovo",
        standard_cost_usd=2700.0,
        depreciation_schedule_months=36,
        mdm_profile="Enterprise FileVault / BitLocker TPM 2.0"
    ),
    "SKU-HW-0297": HardwareAssetProfile(
        asset_sku="SKU-HW-0297",
        model_name="Enterprise Hardware Asset SKU-HW-0297 (Ultra-High Resolution Displays)",
        category="Ultra-High Resolution Displays",
        oem_vendor="Dell / LG / Apple",
        standard_cost_usd=1300.0,
        depreciation_schedule_months=48,
        mdm_profile="Asset Tagged Display Profile"
    ),
    "SKU-HW-0298": HardwareAssetProfile(
        asset_sku="SKU-HW-0298",
        model_name="Enterprise Hardware Asset SKU-HW-0298 (Hardware Security Keys & Tokens)",
        category="Hardware Security Keys & Tokens",
        oem_vendor="Yubico / Google",
        standard_cost_usd=455.0,
        depreciation_schedule_months=60,
        mdm_profile="FIPS 140-2 Level 3 WebAuthn / FIDO2"
    ),
    "SKU-HW-0299": HardwareAssetProfile(
        asset_sku="SKU-HW-0299",
        model_name="Enterprise Hardware Asset SKU-HW-0299 (Thunderbolt Docks & Networking Hubs)",
        category="Thunderbolt Docks & Networking Hubs",
        oem_vendor="CalDigit / Anker",
        standard_cost_usd=800.0,
        depreciation_schedule_months=48,
        mdm_profile="Universal Dock Firmware v2.1"
    ),
    "SKU-HW-0300": HardwareAssetProfile(
        asset_sku="SKU-HW-0300",
        model_name="Enterprise Hardware Asset SKU-HW-0300 (Conference Room Video Hardware)",
        category="Conference Room Video Hardware",
        oem_vendor="Logitech / Poly",
        standard_cost_usd=4500.0,
        depreciation_schedule_months=60,
        mdm_profile="Zoom Rooms / Teams MTR Appliance"
    ),
}

class MasterHardwareService:
    @classmethod
    def get_asset(cls, sku: str) -> HardwareAssetProfile:
        return MASTER_300_HARDWARE_CATALOG.get(sku)

    @classmethod
    def get_all(cls) -> List[HardwareAssetProfile]:
        return list(MASTER_300_HARDWARE_CATALOG.values())
