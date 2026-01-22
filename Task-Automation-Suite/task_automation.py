import os
import shutil
from datetime import datetime

# ------------------- Configuration -------------------

SOURCE_FOLDER = "sample_files"
BACKUP_FOLDER = "backup"
REPORT_FOLDER = "reports"

# ------------------- File Sorting -------------------

def sort_files():
    print("\n[+] Sorting files...")
    try:
        for file in os.listdir(SOURCE_FOLDER):
            path = os.path.join(SOURCE_FOLDER, file)

            if os.path.isfile(path):
                if '.' in file:
                    ext = file.split('.')[-1].upper()
                else:
                    ext = "OTHER"

                dest_folder = os.path.join(SOURCE_FOLDER, ext)
                os.makedirs(dest_folder, exist_ok=True)

                shutil.move(path, os.path.join(dest_folder, file))
                print(f"Moved {file} -> {ext}/")

    except Exception as e:
        print(f"File sorting failed: {e}")

# ------------------- Backup Automation -------------------

def backup_files():
    print("\n[+] Creating backup...")
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(BACKUP_FOLDER, f"backup_{timestamp}")

        os.makedirs(backup_path, exist_ok=True)
        shutil.copytree(SOURCE_FOLDER, backup_path, dirs_exist_ok=True)

        print(f"Backup created at: {backup_path}")

    except Exception as e:
        print(f"Backup failed: {e}")

# ------------------- Report Generation -------------------

def generate_report():
    print("\n[+] Generating report...")
    try:
        total_files = 0
        file_types = {}

        for root, dirs, files in os.walk(SOURCE_FOLDER):
            for file in files:
                total_files += 1
                ext = file.split('.')[-1].lower() if '.' in file else "other"
                file_types[ext] = file_types.get(ext, 0) + 1

        os.makedirs(REPORT_FOLDER, exist_ok=True)

        report_file = os.path.join(
            REPORT_FOLDER,
            f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

        with open(report_file, "w") as f:
            f.write("Task Automation Report\n")
            f.write(f"Generated on: {datetime.now()}\n\n")
            f.write(f"Total Files: {total_files}\n\n")
            f.write("File Type Summary:\n")

            for ext, count in file_types.items():
                f.write(f"{ext}: {count}\n")

        print(f"Report generated: {report_file}")

    except Exception as e:
        print(f"Report generation failed: {e}")

# ------------------- Menu -------------------

def menu():
    while True:
        print("\n====== Task Automation Script Suite ======")
        print("1. Sort Files")
        print("2. Backup Files")
        print("3. Generate Report")
        print("4. Run All")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sort_files()
        elif choice == "2":
            backup_files()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            sort_files()
            backup_files()
            generate_report()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

# ------------------- Main -------------------

if __name__ == "__main__":
    # Create folders if not exist
    os.makedirs(SOURCE_FOLDER, exist_ok=True)
    os.makedirs(BACKUP_FOLDER, exist_ok=True)
    os.makedirs(REPORT_FOLDER, exist_ok=True)

    menu()
