"""
Rename HR Management System to HR Management System across the entire application codebase.
"""
import os
import re

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

# Replacements to make
REPLACEMENTS = [
    ("HR Management System - Enterprise HR Management & Workforce Intelligence Platform", "HR Management System - Enterprise HR Management & Workforce Intelligence Platform"),
    ("HR Management System", "HR Management System"),
    ("HR Management System", "HR Management System"),
    ("HR MANAGEMENT SYSTEM ENTERPRISE", "HR MANAGEMENT SYSTEM ENTERPRISE"),
    ("HR MANAGEMENT SYSTEM", "HR MANAGEMENT SYSTEM"),
    ("HR Management System Global Enterprise Inc.", "HR Management System Global Enterprise Inc."),
    ("HR Management System Global Enterprise", "HR Management System Global Enterprise"),
    ("HR Management System AI Assistant", "HR Management System AI Assistant"),
    ("HR Management System AI", "HR Management System AI"),
    ("HR Management System", "HR Management System"),
    ("hr-management-system", "hr-management-system"),
    ("hr_management_system", "hr_management_system"),
]

def update_file(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception:
        return False, 0

    original = content
    count = 0
    for old, new in REPLACEMENTS:
        if old in content:
            content = content.replace(old, new)
            count += 1

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return True, count
    return False, 0

def main():
    total_updated = 0
    total_replacements = 0
    
    for root, dirs, files in os.walk(BASE_DIR):
        if any(ex in root for ex in [".git", "node_modules", "__pycache__", ".pytest_cache", "dist"]):
            continue
        for file in files:
            if file.endswith((".py", ".ts", ".tsx", ".js", ".jsx", ".html", ".css", ".json", ".yaml", ".yml", ".md", ".toml", ".ini")):
                path = os.path.join(root, file)
                rel = os.path.relpath(path, BASE_DIR)
                updated, count = update_file(path)
                if updated:
                    total_updated += 1
                    total_replacements += count
                    print(f"[REPLACED] {rel} ({count} patterns matched)")

    print(f"\n[FINISHED] Updated {total_updated} files with {total_replacements} total replacements.")

if __name__ == "__main__":
    main()
