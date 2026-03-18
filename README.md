# SharePoint File Upload & Sales ETL Project

This project implements a comprehensive ETL (Extract, Transform, Load) pipeline for:
1. Demo file creation and merging
2. Regional sales data consolidation
3. Data loading to Snowflake and SharePoint

## Structure
- **data_loader.py**: Creates and loads 10 demo files
- **transformer.py**: Merges multiple files into a single file
- **reader.py**: Reads merged file and handles SharePoint upload
- **sales_data_generator.py**: Generates 10 regional sales CSV files
- **sales_merger.py**: Merges all regional sales files into a single consolidated file
- **snowflake_loader.py**: Validates and loads sales data to Snowflake
- **upload_script.py**: Main orchestration script that coordinates the entire pipeline
- **test_upload_script.py**: Unit tests for all components
- **README.md**: Project instructions

## Features
- **Generate Regional Sales Data**: Creates 10 dummy sales files with realistic data from different regions
- **Automatic Merging**: Consolidates all regional files into a single master sales file
- **Data Validation**: Validates data integrity before loading to Snowflake
- **Snowflake Integration**: Loads validated data to Snowflake with proper schema
- **Modular Architecture**: Separate concerns for easy maintenance and testing
- **Test Coverage**: Comprehensive unit tests with 76%+ code coverage

## Requirements
- Python 3.x
- SharePoint access (with API permissions)
- Snowflake account (for data warehouse loading)
- Required Python packages: requests, office365-rest-python-client, pytest, pytest-cov, pandas

## Installation
```bash
pip install requests office365-rest-python-client pytest pytest-cov pandas
pip install snowflake-connector-python  # Optional: for actual Snowflake integration
```

## Configuration

### Snowflake Setup
Update `snowflake_loader.py` with your Snowflake credentials:
```python
SNOWFLAKE_CONFIG = {
    'account': 'your-snowflake-account',
    'user': 'your-username',
    'password': 'your-password',
    'database': 'your_database',
    'schema': 'your_schema',
    'warehouse': 'your_warehouse',
    'role': 'your_role'
}
```

### SharePoint Setup
Update `reader.py` with your SharePoint credentials:
- Replace `SHAREPOINT_SITE_URL` with your SharePoint URL
- Replace `USERNAME` and `PASSWORD` with your credentials
- Replace `SHAREPOINT_LIST_NAME` with your list name

## Usage

### Run Complete Pipeline
```bash
python upload_script.py
```

### Run Individual Components
```bash
# Generate regional sales data
python sales_data_generator.py

# Merge regional sales files
python sales_merger.py

# Validate and load to Snowflake
python snowflake_loader.py

# Or run demo pipeline
python upload_script.py
```

### Run Tests
```bash
pytest --cov=. --cov-fail-under=60
```

## Data Files
- **Location**: `C:\Users\pratyush.panigrahy\OneDrive - drmartens.com\files\`
- **Regional Files**: `sales_{region}.csv` for each of 10 regions
- **Merged File**: `sales_merged_all_regions.csv` (consolidated data)

## Sales Data Columns
- Region: Geographic region of the sale
- Sales_ID: Unique identifier for each sale
- Date: Sale date
- Product: Product sold
- Quantity: Number of units sold
- Unit_Price: Price per unit
- Total_Sale_Amount: Total sale value
- Customer_Name: Name of the customer
- Customer_ID: Unique customer identifier
- Salesperson: Name of the salesperson
- Payment_Method: Method of payment
- Status: Sale status (Completed, Pending, Cancelled)
- Merge_Timestamp: When data was merged
- Data_Source: Source system identifier

## Architecture
The project follows a modular ETL pattern:
- **Data Generator**: Creates realistic sample data
- **Data Loader**: Handles file creation and reading
- **Transformer/Merger**: Processes and consolidates data
- **Reader**: Handles final processing
- **Snowflake Loader**: Manages data warehouse integration
- **Upload Script**: Orchestrates the entire pipeline

## Pre-Push Hook
Code is automatically tested before pushing via pre-push hook:
- Runs pytest with coverage requirement (minimum 60%)
- Validates code quality
- Ensures all tests pass
