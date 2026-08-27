"""
Enterprise Codebase Scale Generator & Domain Engine Builder
Constructs high-depth enterprise algorithms, business logic, rules, and components.
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ensure_file(rel_path, content):
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {rel_path} ({len(content.splitlines())} lines)")


if __name__ == "__main__":
    print("Building Domain Engines...")
