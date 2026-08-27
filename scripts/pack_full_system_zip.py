"""
Package HR Management System.zip ensuring .git directory and full git history are included.
"""
import os
import zipfile

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"
ZIP_PATH = os.path.join(BASE_DIR, "HR Management System.zip")

def package_zip():
    print(f"Creating archive at: {ZIP_PATH}")
    
    # Remove existing zip if present
    if os.path.exists(ZIP_PATH):
        try:
            os.remove(ZIP_PATH)
        except Exception as e:
            print(f"Notice: {e}")

    total_files = 0
    total_uncompressed_bytes = 0

    with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
        for root, dirs, files in os.walk(BASE_DIR):
            # Exclude ephemeral node_modules, pycache, dist, and zip file itself
            rel_root = os.path.relpath(root, BASE_DIR)
            
            # Skip node_modules, __pycache__, .pytest_cache
            if any(part in ('node_modules', '__pycache__', '.pytest_cache', '.turbo', '.next') for part in rel_root.split(os.sep)):
                continue

            for file in files:
                if file == "HR Management System.zip" or file.endswith(".tmp"):
                    continue
                
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, BASE_DIR)
                
                # Write file to zip
                zipf.write(full_path, rel_path)
                total_files += 1
                total_uncompressed_bytes += os.path.getsize(full_path)

    zip_size_mb = os.path.getsize(ZIP_PATH) / (1024 * 1024)
    print(f"[SUCCESS] Packaged {total_files} files into '{os.path.basename(ZIP_PATH)}'")
    print(f"Total Size: {zip_size_mb:.2f} MB (Uncompressed: {total_uncompressed_bytes / (1024*1024):.2f} MB)")

    # Verify .git is inside zip
    with zipfile.ZipFile(ZIP_PATH, 'r') as check_zip:
        git_entries = [name for name in check_zip.namelist() if name.startswith('.git/')]
        print(f"Verification: Found {len(git_entries)} .git entries in the zip archive!")

if __name__ == "__main__":
    package_zip()
