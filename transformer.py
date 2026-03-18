import os
from data_loader import load_demo_files, DEMO_FILE_PATHS

# Transformer Script - Merges demo files into one
MERGED_FILE_PATH = "merged_demo_file.txt"

def merge_files():
    """Merge all demo files into a single merged file."""
    with open(MERGED_FILE_PATH, 'w') as merged_file:
        for demo_path in DEMO_FILE_PATHS:
            try:
                with open(demo_path, 'r') as f:
                    content = f.read()
                    merged_file.write(content)
                    print(f"Merged: {demo_path}")
            except FileNotFoundError:
                print(f"File not found during merge: {demo_path}")
    print(f"Merged file created: {MERGED_FILE_PATH}")

def transform_data(input_files):
    """Transform loaded data and return statistics."""
    stats = {
        'total_files': len(input_files),
        'total_size': sum(len(content) for content in input_files.values()),
        'file_count': len(input_files)
    }
    return stats

if __name__ == "__main__":
    contents = load_demo_files()
    merge_files()
    stats = transform_data(contents)
    print(f"Transform stats: {stats}")
