import os
import pandas as pd
from datetime import datetime

# Configuration
INPUT_DIR = r"C:\Users\pratyush.panigrahy\OneDrive - drmartens.com\files"
OUTPUT_FILE = os.path.join(INPUT_DIR, "sales_merged_all_regions.csv")

def merge_regional_sales():
    """Merge all regional sales CSV files into a single file."""
    if not os.path.exists(INPUT_DIR):
        print(f"Error: Directory not found: {INPUT_DIR}")
        return None
    
    # Get all sales files
    sales_files = [f for f in os.listdir(INPUT_DIR) if f.startswith("sales_") and f.endswith(".csv") and f != "sales_merged_all_regions.csv"]
    
    if not sales_files:
        print(f"No sales files found in {INPUT_DIR}")
        return None
    
    print(f"Found {len(sales_files)} regional sales files\n")
    
    # Merge all files
    merged_df = pd.DataFrame()
    
    for file in sorted(sales_files):
        filepath = os.path.join(INPUT_DIR, file)
        try:
            df = pd.read_csv(filepath)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
            print(f"Merged: {file} ({len(df)} records)")
        except Exception as e:
            print(f"Error reading {file}: {e}")
    
    if merged_df.empty:
        print("Error: No data to merge")
        return None
    
    # Add metadata columns
    merged_df['Merge_Timestamp'] = datetime.now().isoformat()
    merged_df['Data_Source'] = 'Regional_Sales'
    
    # Save merged file
    try:
        merged_df.to_csv(OUTPUT_FILE, index=False)
        print(f"\n✓ Merged file created: {OUTPUT_FILE}")
        print(f"  - Total records: {len(merged_df)}")
        print(f"  - Total sales: ${merged_df['Total_Sale_Amount'].sum():,.2f}")
        print(f"  - Columns: {len(merged_df.columns)}")
        return OUTPUT_FILE
    except Exception as e:
        print(f"Error saving merged file: {e}")
        return None

def load_merged_sales():
    """Load and return the merged sales data."""
    try:
        if os.path.exists(OUTPUT_FILE):
            df = pd.read_csv(OUTPUT_FILE)
            print(f"Loaded merged sales file: {len(df)} records")
            return df
        else:
            print(f"Merged file not found: {OUTPUT_FILE}")
            return None
    except Exception as e:
        print(f"Error loading merged file: {e}")
        return None

if __name__ == "__main__":
    print("=== Merging Regional Sales Data ===\n")
    merge_regional_sales()
    print("\n=== Merge Complete ===")
