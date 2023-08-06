import os
import shutil
import platform
import time

def get_system_directories():
    if platform.system() == 'Windows':
        return {
            'Documents': os.path.expanduser('~\\Documents'),
            'Pictures': os.path.expanduser('~\\Pictures'),
            'Music': os.path.expanduser('~\\Music'),
            'Videos': os.path.expanduser('~\\Videos')
        }
    elif platform.system() == 'Linux':
        return {
            'Documents': os.path.expanduser('~/Documents'),
            'Pictures': os.path.expanduser('~/Pictures'),
            'Music': os.path.expanduser('~/Music'),
            'Videos': os.path.expanduser('~/Videos')
        }
    elif platform.system() == 'Darwin':  # Mac
        return {
            'Documents': os.path.expanduser('~/Documents'),
            'Pictures': os.path.expanduser('~/Pictures'),
            'Music': os.path.expanduser('~/Music'),
            'Videos': os.path.expanduser('~/Movies')
        }
    else:
        raise Exception("Unsupported OS")

def move_files(source_dir, target_dirs):
    files_moved = []
    files_not_moved = []

    for root, _, files in os.walk(source_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_extension = os.path.splitext(filename)[1][1:].lower()

            if file_extension:
                target_dir = target_dirs.get(file_extension, None)
                if target_dir:
                    try:
                        modified_time = os.path.getmtime(file_path)
                        current_time = time.time()
                        days_since_modified = (current_time - modified_time) / (60 * 60 * 24)

                        if days_since_modified > 30:
                            target_dir = os.path.join(source_dir, 'old_files')
                            os.makedirs(target_dir, exist_ok=True)
                        else:
                            target_dir = target_dirs[file_extension]
                        
                        target_path = os.path.join(target_dir, filename)
                        shutil.move(file_path, target_path)
                        files_moved.append((filename, target_path))
                    except Exception as e:
                        files_not_moved.append((filename, str(e)))
                else:
                    files_not_moved.append((filename, "Unsupported file extension"))
            else:
                files_not_moved.append((filename, "No file extension"))

    return files_moved, files_not_moved

def main():
    source_dir = input("Enter the source directory: ")
    target_dirs = get_system_directories()

    if not os.path.exists(source_dir):
        print("Source directory does not exist.")
        return

    files_moved, files_not_moved = move_files(source_dir, target_dirs)

    print("\nFiles moved:")
    for filename, target_path in files_moved:
        print(f"{filename} moved to {target_path}")

    print("\nFiles not moved:")
    for filename, reason in files_not_moved:
        print(f"{filename}: {reason}")

if __name__ == "__main__":
    main()