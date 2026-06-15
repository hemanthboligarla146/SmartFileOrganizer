import os
from config import file_types
from datetime import datetime
# Determine category
def get_category(extension):

    if extension in file_types:
        return file_types[extension]
        
    # Create folder dynamically for unknown extensions
    category = extension[1:].upper()

    # Handle files with no extension
    if category == "":
        return "NO_EXTENSION"
    return category
 

# Create category folder if it doesn't exist
def create_category(category):
    if not os.path.exists(category):
        os.mkdir(category)
        print(f"{category} folder created")

# Handle duplicate filenames
def get_unique_destination(destination_path, category, name, extension):

    counter = 1

    while os.path.exists(destination_path):

        new_file_name = f"{name}_{counter}{extension}"

        destination_path = os.path.join(
            category,
            new_file_name
        )

        counter += 1
    return destination_path

def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("organizer.log", "a") as file:
        file.write(f"{timestamp} - {message}\n")


def backup_file(source_path):
    pass