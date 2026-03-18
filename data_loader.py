import os

# Data Loader Script - Creates and manages demo files
DEMO_FILE_PATHS = [f"demo_file_{i}.txt" for i in range(1, 11)]

def create_demo_files():
    """Create 10 demo files if they don't exist."""
    for i, demo_path in enumerate(DEMO_FILE_PATHS, 1):
        content = f"This is the content of demo file {i}.\n"
        try:
            with open(demo_path, 'x') as f:
                f.write(content)
                print(f"Created: {demo_path}")
        except FileExistsError:
            print(f"File already exists: {demo_path}")

def load_demo_files():
    """Load and return content of all demo files."""
    file_contents = {}
    for demo_path in DEMO_FILE_PATHS:
        try:
            with open(demo_path, 'r') as f:
                file_contents[demo_path] = f.read()
        except FileNotFoundError:
            print(f"File not found: {demo_path}")
    return file_contents

if __name__ == "__main__":
    create_demo_files()
    contents = load_demo_files()
    print(f"Loaded {len(contents)} demo files")
