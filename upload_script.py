# Main orchestration script - coordinates data loading, transformation, and reading
from data_loader import create_demo_files, load_demo_files
from transformer import merge_files, transform_data
from reader import read_merged_file, upload_to_sharepoint

def main():
    """Main function to orchestrate the ETL pipeline."""
    print("=== Starting ETL Pipeline ===\n")
    
    # Step 1: Load data
    print("Step 1: Loading data...")
    create_demo_files()
    loaded_files = load_demo_files()
    print(f"Loaded {len(loaded_files)} files\n")
    
    # Step 2: Transform data
    print("Step 2: Transforming data...")
    merge_files()
    stats = transform_data(loaded_files)
    print(f"Transform stats: {stats}\n")
    
    # Step 3: Read and process
    print("Step 3: Reading and processing...")
    content = read_merged_file()
    if content:
        print(f"Merged file size: {len(content)} bytes")
        print("\n=== ETL Pipeline Complete ===")
        # Uncomment below to upload to SharePoint
        # upload_to_sharepoint("merged_demo_file.txt")

if __name__ == "__main__":
    main()
