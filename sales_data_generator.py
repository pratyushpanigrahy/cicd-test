import os
import pandas as pd
from datetime import datetime, timedelta
import random

# Configuration
OUTPUT_DIR = r"C:\Users\pratyush.panigrahy\OneDrive - drmartens.com\files"
REGIONS = ["North", "South", "East", "West", "Northeast", "Northwest", "Southeast", "Southwest", "Central", "Coastal"]
PRODUCTS = ["Product A", "Product B", "Product C", "Product D", "Product E"]
SALESPEOPLE = ["John Smith", "Sarah Johnson", "Michael Brown", "Emily Davis", "Robert Wilson", "Lisa Anderson", "David Martinez", "Jennifer Taylor", "James Thomas", "Maria Garcia"]
PAYMENT_METHODS = ["Credit Card", "Cash", "Check", "Bank Transfer", "PayPal"]
STATUSES = ["Completed", "Pending", "Cancelled"]

def generate_sales_data(region, num_records=50, region_index=0):
    """Generate dummy sales data for a region."""
    start_date = datetime(2024, 1, 1)
    
    data = {
        'Region': [region] * num_records,
        'Sales_ID': [f"SALE-{region_index:02d}-{i+1:05d}" for i in range(num_records)],
        'Date': [start_date + timedelta(days=random.randint(0, 365)) for _ in range(num_records)],
        'Product': [random.choice(PRODUCTS) for _ in range(num_records)],
        'Quantity': [random.randint(1, 50) for _ in range(num_records)],
        'Unit_Price': [round(random.uniform(10, 500), 2) for _ in range(num_records)],
        'Customer_Name': [f"Customer_{i+1}" for i in range(num_records)],
        'Customer_ID': [f"CUST-{i+1:05d}" for i in range(num_records)],
        'Salesperson': [random.choice(SALESPEOPLE) for _ in range(num_records)],
        'Payment_Method': [random.choice(PAYMENT_METHODS) for _ in range(num_records)],
        'Status': [random.choice(STATUSES) for _ in range(num_records)]
    }
    
    df = pd.DataFrame(data)
    df['Total_Sale_Amount'] = df['Quantity'] * df['Unit_Price']
    df = df[['Region', 'Sales_ID', 'Date', 'Product', 'Quantity', 'Unit_Price', 'Total_Sale_Amount', 'Customer_Name', 'Customer_ID', 'Salesperson', 'Payment_Method', 'Status']]
    
    return df

def create_sales_files():
    """Create 10 regional sales files."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}\n")
    
    for idx, region in enumerate(REGIONS):
        df = generate_sales_data(region, region_index=idx)
        filename = os.path.join(OUTPUT_DIR, f"sales_{region.lower()}.csv")
        df.to_csv(filename, index=False)
        print(f"Created: {filename}")
        print(f"  - Records: {len(df)}")
        print(f"  - Total Sales: ${df['Total_Sale_Amount'].sum():,.2f}\n")

if __name__ == "__main__":
    print("=== Generating Regional Sales Data ===\n")
    create_sales_files()
    print("=== Sales data generation complete ===")
