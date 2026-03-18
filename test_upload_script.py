import os
import pytest
from unittest import mock

MERGED_FILE_PATH = "merged_demo_file.txt"
DEMO_FILE_PATHS = [f"demo_file_{i}.txt" for i in range(1, 11)]
SALES_MERGED_FILE = r"C:\Users\pratyush.panigrahy\OneDrive - drmartens.com\files\sales_merged_all_regions.csv"

@pytest.fixture(autouse=True)
def cleanup_files():
    # Remove demo and merged files before and after each test
    for path in DEMO_FILE_PATHS + [MERGED_FILE_PATH]:
        if os.path.exists(path):
            os.remove(path)
    yield
    for path in DEMO_FILE_PATHS + [MERGED_FILE_PATH]:
        if os.path.exists(path):
            os.remove(path)

def test_data_loader_creates_files():
    from data_loader import create_demo_files, DEMO_FILE_PATHS
    create_demo_files()
    for i, path in enumerate(DEMO_FILE_PATHS, 1):
        assert os.path.exists(path)
        with open(path) as f:
            assert f.read() == f"This is the content of demo file {i}.\n"

def test_transformer_merges_files():
    from data_loader import create_demo_files, DEMO_FILE_PATHS
    from transformer import merge_files, MERGED_FILE_PATH
    create_demo_files()
    merge_files()
    merged_content = "".join([f"This is the content of demo file {i}.\n" for i in range(1, 11)])
    with open(MERGED_FILE_PATH) as f:
        assert f.read() == merged_content

def test_reader_reads_merged_file():
    from data_loader import create_demo_files, DEMO_FILE_PATHS
    from transformer import merge_files
    from reader import read_merged_file
    create_demo_files()
    merge_files()
    content = read_merged_file()
    assert content is not None
    assert len(content) > 0
    assert "demo file 1" in content

def test_upload_script_main():
    from upload_script import main
    main()
    assert os.path.exists(MERGED_FILE_PATH)

def test_sales_merger_merges_files():
    from sales_merger import merge_regional_sales
    merged_file = merge_regional_sales()
    if merged_file:
        assert os.path.exists(merged_file)
        import pandas as pd
        df = pd.read_csv(merged_file)
        assert len(df) > 0
        assert 'Sales_ID' in df.columns
        assert 'Region' in df.columns

def test_snowflake_loader_validates_data():
    if os.path.exists(SALES_MERGED_FILE):
        from snowflake_loader import validate_data
        assert validate_data(SALES_MERGED_FILE) == True
