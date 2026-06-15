import os
import shutil
from organizer import (get_category, create_category, get_unique_destination, write_log)


# Move file
def move_file(source_path, destination_path):
    shutil.move(source_path, destination_path)

source_folder = "test_folder"

files = os.listdir(source_folder)
report = {}
for file in files:

    # Full path of the current file
    source_path = os.path.join(source_folder, file)

    # Skip folders if any exist inside test_folder
    if not os.path.isfile(source_path):
        continue

    # Split filename and extension
    name, extension = os.path.splitext(file)

    # Convert extension to lowercase
    extension = extension.lower()

    category = get_category(extension)
    create_category(category)
    
    # Destination path
    destination_path = os.path.join(category, file)
    
    # Handle duplicate filenames
    destination_path = get_unique_destination(destination_path, category, name, extension)

    # move the file to the destination path    
    move_file(source_path, destination_path)
    write_log(f"{file} moved to {category}")
    
    if category in report:
        report[category] += 1
    else:
        report[category] = 1

    print(f"{file} moved to {category}")

    

print("\n===== ORGANIZTION REPORT =====")
for category, count in report.items():
    print(f"{category}: {count}")

total_files = sum(report.values())
print(f"\nTotal Files: {total_files}")




