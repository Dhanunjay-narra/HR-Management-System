"""
Full Scale Enterprise Platform Generator
Generates comprehensive domain logic, calculation engines, rules, and React TypeScript components.
"""
import os
import sys

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write_file(rel_path, content):
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {rel_path} ({len(content.splitlines())} lines)")

if __name__ == "__main__":
    print("Beginning generator execution...")
