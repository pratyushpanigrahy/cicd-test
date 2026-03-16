import os
import pytest

def test_dummy():
    assert True

def test_upload_script_exists():
    assert os.path.exists("upload_script.py")

def test_excel_file_created():
    # This test will pass if dummy_table.xlsx exists after running test_upload_excel.py
    assert os.path.exists("dummy_table.xlsx")
