"""
Comprehensive Enterprise Codebase Generator
Generates full-scale production domain engines, calculators, algorithms, and React TypeScript modules.
"""
import os
import sys

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def ensure_file(rel_path, content):
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {rel_path} ({len(content.splitlines())} lines)")

print("Generator script template ready.")
