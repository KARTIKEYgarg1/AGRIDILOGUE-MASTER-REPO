import os

def rename_and_copy(source_dir):
    if not os.path.exists(source_dir):
        print("Directory does not exist.")
        return

    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        if os.path.isfile(item_path):
            if item.endswith('.txt'):
                new_file = os.path.join(source_dir, item.replace(' ', '_'))
                os.rename(item_path, new_file)
                print(f"Renamed file '{item}' to '{item.replace(' ', '_')}'")

                # Copy content to a new file without spaces in the filename
                with open(new_file, 'r') as file:
                    content = file.read()
                    new_filename = new_file.replace('.txt', '_new.txt')
                    with open(new_filename, 'w') as new_file:
                        new_file.write(content)
                        print(f"Created new file '{new_filename}' without spaces")
        elif os.path.isdir(item_path):
            new_dir = os.path.join(source_dir, item.replace(' ', '_'))
            os.rename(item_path, new_dir)
            print(f"Renamed directory '{item}' to '{item.replace(' ', '_')}'")

# Example usage:
source_directory = 'VIKASPEDIA_DATA'  # Replace with the actual directory name
rename_and_copy(source_directory)
