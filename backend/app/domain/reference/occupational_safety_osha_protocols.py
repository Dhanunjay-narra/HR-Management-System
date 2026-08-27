"""
OSHA 1910 General Industry Occupational Safety & Health Protocols
Standard protocols for ergonomic evaluations, hazard communication, emergency evacuation, and first aid.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class WorkplaceSafetyProtocol:
    protocol_code: str
    title: str
    environment_scope: str
    mandatory_compliance_rules: List[str]


MASTER_OSHA_PROTOCOLS: Dict[str, WorkplaceSafetyProtocol] = {
    "OSHA-01": WorkplaceSafetyProtocol(
        protocol_code="OSHA-01",
        title="Ergonomics & Workstation VDT Standard",
        environment_scope="Office & Remote Work",
        mandatory_compliance_rules=['Annual ergonomic self-assessment submission.', 'Adjustable chair with lumbar support and monitor positioned at eye level.', 'Mandatory 5-minute micro-breaks every 60 minutes of continuous screen work.']
    ),
    "OSHA-02": WorkplaceSafetyProtocol(
        protocol_code="OSHA-02",
        title="Emergency Evacuation & Severe Weather Action Plan",
        environment_scope="Facility Safety",
        mandatory_compliance_rules=['Clearly marked, unobstructed emergency exit egress routes in all office facilities.', 'Bi-annual evacuation drills led by designated floor wardens.', 'Primary and secondary designated meeting locations outside the building.']
    ),
    "OSHA-03": WorkplaceSafetyProtocol(
        protocol_code="OSHA-03",
        title="Hazard Communication & Chemical Safety (SDS)",
        environment_scope="Facility & Lab",
        mandatory_compliance_rules=['Safety Data Sheets (SDS) accessible digitally 24/7 to all personnel.', 'Appropriate PPE (nitrile gloves, splash goggles) required when handling cleaning reagents.', 'Secondary container labeling conforming to GHS hazard pictograms.']
    ),
    "OSHA-04": WorkplaceSafetyProtocol(
        protocol_code="OSHA-04",
        title="Electrical Safety & Portable Appliance Testing (PAT)",
        environment_scope="General Safety",
        mandatory_compliance_rules=['Prohibition of daisy-chained power strips and ungrounded extension cords.', 'Immediate reporting and replacement of frayed power cables.', 'Annual thermal inspection of electrical breaker panels by licensed electricians.']
    ),
    "OSHA-05": WorkplaceSafetyProtocol(
        protocol_code="OSHA-05",
        title="Bloodborne Pathogens & First Aid Kit Maintenance",
        environment_scope="Health & Safety",
        mandatory_compliance_rules=['Fully stocked ANSI/ISEA Z308.1-2021 Type I First Aid Kits on every office floor.', 'Automated External Defibrillator (AED) units inspected monthly with certified CPR staff.', 'Universal precautions for biohazard response with certified hazardous waste disposal.']
    ),
}

class SafetyProtocolService:
    @classmethod
    def get_protocol(cls, code: str) -> WorkplaceSafetyProtocol:
        return MASTER_OSHA_PROTOCOLS.get(code)

    @classmethod
    def get_all_protocols(cls) -> List[WorkplaceSafetyProtocol]:
        return list(MASTER_OSHA_PROTOCOLS.values())
