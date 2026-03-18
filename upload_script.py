# Main orchestration script - coordinates data loading, transformation, and reading
from data_loader import create_demo_files, load_demo_files
from transformer import merge_files, transform_data
from reader import read_merged_file, upload_to_sharepoint
from sales_merger import merge_regional_sales, load_merged_sales
from snowflake_loader import validate_data, load_to_snowflake, SNOWFLAKE_CONFIG

def main():
    """Main function to orchestrate the ETL pipeline."""
    print("=== Starting ETL Pipeline ===\n")
    
    # Step 1: Load demo data
    print("Step 1: Loading demo data...")
    create_demo_files()
    loaded_files = load_demo_files()
    print(f"Loaded {len(loaded_files)} files\n")
    
    # Step 2: Transform demo data
    print("Step 2: Transforming demo data...")
    merge_files()
    stats = transform_data(loaded_files)
    print(f"Transform stats: {stats}\n")
    
    # Step 3: Read demo data
    print("Step 3: Reading and processing demo data...")
    content = read_merged_file()
    if content:
        print(f"Merged demo file size: {len(content)} bytes\n")
    
    # Step 4: Process sales data
    print("Step 4: Merging regional sales data...")
    merged_sales_file = merge_regional_sales()
    print()
    
    if merged_sales_file:
        # Step 5: Validate sales data
        print("Step 5: Validating sales data...")
        if validate_data(merged_sales_file):
            # Step 6: Load to Snowflake
            print("\nStep 6: Loading sales data to Snowflake...")
            load_to_snowflake(merged_sales_file, **SNOWFLAKE_CONFIG)
    
    print("\n=== ETL Pipeline Complete ===")

if __name__ == "__main__":
    main()
