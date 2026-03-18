# SharePoint File Upload Project

This project implements an ETL (Extract, Transform, Load) pipeline for uploading files to SharePoint with modular architecture.

## Structure
- **data_loader.py**: Creates and loads 10 demo files
- **transformer.py**: Merges multiple files into a single file
- **reader.py**: Reads merged file and handles SharePoint upload
- **upload_script.py**: Main orchestration script that coordinates the pipeline
- **test_upload_script.py**: Unit tests for all components
- **README.md**: Project instructions

## Requirements
- Python 3.x
- SharePoint access (with API permissions)
- Required Python packages: requests, office365-rest-python-client, pytest, pytest-cov

## Usage
1. Configure SharePoint credentials in reader.py:
   - Replace `SHAREPOINT_SITE_URL` with your SharePoint URL
   - Replace `USERNAME` and `PASSWORD` with your credentials
   - Replace `SHAREPOINT_LIST_NAME` with your list name

2. Run the main orchestration script:
   ```
   python upload_script.py
   ```

3. Or run individual modules:
   ```
   python data_loader.py    # Create demo files
   python transformer.py     # Merge demo files
   python reader.py         # Read and optionally upload to SharePoint
   ```

## Setup
Install dependencies:
```
pip install requests office365-rest-python-client pytest pytest-cov
```

## Testing
Run all tests with coverage:
```
pytest --cov=. --cov-fail-under=60
```

## Architecture
The project follows a modular ETL pattern:
- **Data Loader**: Handles file creation and reading
- **Transformer**: Processes and merges data
- **Reader**: Handles final processing and SharePoint integration
- **Upload Script**: Orchestrates the entire pipeline

This separation of concerns makes the code more maintainable and testable.
