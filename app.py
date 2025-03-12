file_system = {
    "Pictures": {
        "Saved Pictures": {
            "Web Images": {
                "Chrome": {},
                "Opera": {},
                "Firefox": {}
            }
        },
        "Screenshots": {},
        "Camera Roll": {
            "2025": {},
            "2024": {},
            "2023": {}
        }
    }
}


def add_directory(file_system, path, dir_name):
    current = file_system
    for folder in path:
        if folder in current:
            current = current[folder]
        else:
            print("path not found!")
            return
        if dir_name not in current:
            current[dir_name] = {}
            print(f"'{dir_name}' added")
        else:
            print(f"'{dir_name}' already exists")


def delete_directory(file_system, path, dir_name):
    current = file_system
    for folder in path:
        if folder in current:
            current = current[folder]
        else:
            print("path not found!")
            return
        if dir_name in current:
            del current[dir_name]
            print(f" '{dir_name}' deleted")
        else:
            print("directory not found!")


def display_structure(file_system, level=0):
    for folder, subfolders in file_system.items():
        print(" " * level + f" {folder}")
        display_structure(subfolders, level + 1)


# Example Usage

# Display the initial structure
print(" Initial Directory Structure:")
display_structure(file_system)

# Add a directory
add_directory(file_system, ["Pictures",
              "Saved Pictures", "Web Images"], "Safari")

# Delete a directory
delete_directory(file_system, ["Pictures", "Saved Pictures"], "Web Images")

# Display the updated structure
print("\n Updated Directory Structure:")
display_structure(file_system)
