import pandas as pd
import os

# Dummy Excel table setup
EXCEL_FILE = "dummy_table.xlsx"

# Create a dummy Excel file if it doesn't exist
if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame({
        'Title': ['Sample File'],
        'FileName': ['file.txt'],
        'Status': ['Uploaded']
    })
    df.to_excel(EXCEL_FILE, index=False)
    print(f"Created dummy Excel file: {EXCEL_FILE}")
else:
    print(f"Dummy Excel file already exists: {EXCEL_FILE}")

# Simulate file upload and append metadata
uploaded_file = 'file.txt'  # Placeholder for uploaded file
metadata = {'Title': 'Sample File', 'FileName': uploaded_file, 'Status': 'Uploaded'}

# Append metadata to Excel table using pd.concat for pandas 2.x compatibility
existing_df = pd.read_excel(EXCEL_FILE)
new_row = pd.DataFrame([metadata])
existing_df = pd.concat([existing_df, new_row], ignore_index=True)
existing_df.to_excel(EXCEL_FILE, index=False)
print(f"Appended metadata for '{uploaded_file}' to Excel table.")
