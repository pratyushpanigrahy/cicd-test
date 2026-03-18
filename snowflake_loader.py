import pandas as pd
import os

# Configuration - Update with your Snowflake credentials
SNOWFLAKE_CONFIG = {
    'account': 'your-snowflake-account',
    'user': 'your-username',
    'password': 'your-password',
    'database': 'your_database',
    'schema': 'your_schema',
    'warehouse': 'your_warehouse',
    'role': 'your_role'
}

TABLE_NAME = 'SALES_DATA'

def load_to_snowflake(data_file, **config):
    """Load CSV data to Snowflake table."""
    try:
        # Read the CSV file
        df = pd.read_csv(data_file)
        print(f"Read data file: {data_file}")
        print(f"  - Records: {len(df)}")
        print(f"  - Columns: {len(df.columns)}")
        
        # Try to import snowflake connector
        try:
            from snowflake.connector.pandas_tools import write_pandas
            from snowflake.connector import connect
        except ImportError:
            print("\n⚠ Snowflake connector not installed")
            print("  Install with: pip install snowflake-connector-python")
            print("\n  For now, showing data preview that would be loaded to Snowflake:\n")
            print(df.head(10).to_string())
            return False
        
        # Connect to Snowflake
        print("\n⚠ Snowflake connection not configured yet")
        print("  Please update SNOWFLAKE_CONFIG with your credentials")
        print("  Sample connection code:")
        print("""
        ctx = connect(
            account=config['account'],
            user=config['user'],
            password=config['password'],
            database=config['database'],
            schema=config['schema'],
            warehouse=config['warehouse'],
            role=config['role']
        )
        """)
        
        # Show schema that would be created
        print(f"\nSchema for table '{TABLE_NAME}':")
        print(df.dtypes)
        
        return True
        
    except Exception as e:
        print(f"Error loading to Snowflake: {e}")
        return False

def validate_data(data_file):
    """Validate data before loading to Snowflake."""
    try:
        df = pd.read_csv(data_file)
        
        # Check for required columns
        required_columns = [
            'Region', 'Sales_ID', 'Date', 'Product', 'Quantity',
            'Unit_Price', 'Total_Sale_Amount', 'Customer_Name',
            'Customer_ID', 'Salesperson', 'Payment_Method', 'Status'
        ]
        
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"✗ Missing columns: {missing_columns}")
            return False
        
        # Check for duplicates
        if df.duplicated(subset=['Sales_ID']).any():
            print(f"✗ Duplicate Sales_IDs found")
            return False
        
        # Check for null values
        null_counts = df.isnull().sum()
        if null_counts.sum() > 0:
            print(f"⚠ Null values found:")
            print(null_counts[null_counts > 0])
        
        print(f"✓ Data validation passed")
        print(f"  - Total records: {len(df)}")
        print(f"  - Valid Sales_IDs: {df['Sales_ID'].nunique()}")
        return True
        
    except Exception as e:
        print(f"Error validating data: {e}")
        return False

if __name__ == "__main__":
    print("=== Snowflake Data Loader ===\n")
    
    # Define merged file path
    merged_file = r"C:\Users\pratyush.panigrahy\OneDrive - drmartens.com\files\sales_merged_all_regions.csv"
    
    if os.path.exists(merged_file):
        print("Step 1: Validating data...")
        if validate_data(merged_file):
            print("\nStep 2: Loading to Snowflake...")
            load_to_snowflake(merged_file, **SNOWFLAKE_CONFIG)
    else:
        print(f"File not found: {merged_file}")
        print("Please run sales_merger.py first")
