"""
Enterprise IT Hardware & Workstation Equipment Specifications Catalog
Standard corporate device profiles, warranty lifecycles, MDM security configurations, and procurement costs.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class EnterpriseHardwareItem:
    item_code: str
    model_name: str
    category: str
    procurement_cost_usd: float
    refresh_cycle_months: int
    supported_os: str
    security_standard: str


ENTERPRISE_HARDWARE_CATALOG: Dict[str, EnterpriseHardwareItem] = {
    "HW-MBP-16-M3": EnterpriseHardwareItem(
        item_code="HW-MBP-16-M3",
        model_name="Apple MacBook Pro 16" (M3 Max, 64GB Unified RAM, 1TB SSD)",
        category="Laptops",
        procurement_cost_usd=3499.0,
        refresh_cycle_months=36,
        supported_os="macOS Sonoma / Sequoia",
        security_standard="FileVault 256-bit XTS-AES Enabled"
    ),
    "HW-MBP-14-M3": EnterpriseHardwareItem(
        item_code="HW-MBP-14-M3",
        model_name="Apple MacBook Pro 14" (M3 Pro, 36GB Unified RAM, 512GB SSD)",
        category="Laptops",
        procurement_cost_usd=2399.0,
        refresh_cycle_months=36,
        supported_os="macOS Sonoma / Sequoia",
        security_standard="FileVault 256-bit XTS-AES Enabled"
    ),
    "HW-MBA-15-M3": EnterpriseHardwareItem(
        item_code="HW-MBA-15-M3",
        model_name="Apple MacBook Air 15" (M3, 16GB RAM, 512GB SSD)",
        category="Laptops",
        procurement_cost_usd=1499.0,
        refresh_cycle_months=36,
        supported_os="macOS Sonoma / Sequoia",
        security_standard="FileVault 256-bit XTS-AES Enabled"
    ),
    "HW-DELL-XPS16": EnterpriseHardwareItem(
        item_code="HW-DELL-XPS16",
        model_name="Dell XPS 16 (Intel Core Ultra 9, 32GB RAM, 1TB SSD, RTX 4070)",
        category="Laptops",
        procurement_cost_usd=2899.0,
        refresh_cycle_months=36,
        supported_os="Ubuntu Linux 24.04 LTS / Windows 11 Enterprise",
        security_standard="BitLocker TPM 2.0 / LUKS Encrypted"
    ),
    "HW-THINK-X1": EnterpriseHardwareItem(
        item_code="HW-THINK-X1",
        model_name="Lenovo ThinkPad X1 Carbon Gen 12 (32GB RAM, 1TB SSD)",
        category="Laptops",
        procurement_cost_usd=2199.0,
        refresh_cycle_months=36,
        supported_os="Windows 11 Enterprise",
        security_standard="BitLocker TPM 2.0 Enabled"
    ),
    "HW-MON-DELL32": EnterpriseHardwareItem(
        item_code="HW-MON-DELL32",
        model_name="Dell UltraSharp 32" 4K USB-C Hub Monitor (U3223QE)",
        category="Monitors",
        procurement_cost_usd=899.0,
        refresh_cycle_months=48,
        supported_os="Firmware v1.04",
        security_standard="Asset Tagged"
    ),
    "HW-MON-STUDIO": EnterpriseHardwareItem(
        item_code="HW-MON-STUDIO",
        model_name="Apple Studio Display 27" 5K Retina (Tilt-Adjustable Stand)",
        category="Monitors",
        procurement_cost_usd=1599.0,
        refresh_cycle_months=48,
        supported_os="Apple Display Firmware",
        security_standard="Asset Tagged"
    ),
    "HW-SEC-YUBI5C": EnterpriseHardwareItem(
        item_code="HW-SEC-YUBI5C",
        model_name="YubiKey 5C NFC FIDO2 / WebAuthn Hardware Security Key",
        category="Security Hardware",
        procurement_cost_usd=55.0,
        refresh_cycle_months=60,
        supported_os="Firmware 5.4.3",
        security_standard="FIPS 140-2 Level 3 Validated"
    ),
    "HW-DOCK-CALD4": EnterpriseHardwareItem(
        item_code="HW-DOCK-CALD4",
        model_name="CalDigit TS4 Thunderbolt 4 Dock (18 Ports, 98W Power Delivery)",
        category="Peripherals",
        procurement_cost_usd=399.0,
        refresh_cycle_months=48,
        supported_os="Universal TB4",
        security_standard="Asset Tagged"
    ),
}

class HardwareCatalogService:
    @classmethod
    def get_hardware_item(cls, code: str) -> EnterpriseHardwareItem:
        return ENTERPRISE_HARDWARE_CATALOG.get(code)

    @classmethod
    def get_all_hardware(cls) -> List[EnterpriseHardwareItem]:
        return list(ENTERPRISE_HARDWARE_CATALOG.values())
