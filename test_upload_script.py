import os
import pytest
from unittest import mock

SCRIPT_PATH = "upload_script.py"
MERGED_FILE_PATH = "merged_demo_file.txt"
DEMO_FILE_PATHS = [f"demo_file_{i}.txt" for i in range(1, 11)]

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

def test_demo_files_created():
    import importlib.util
    spec = importlib.util.spec_from_file_location("upload_script", SCRIPT_PATH)
    upload_script = importlib.util.module_from_spec(spec)
    with mock.patch("office365.runtime.auth.authentication_context.AuthenticationContext.acquire_token_for_user", return_value=False):
        spec.loader.exec_module(upload_script)
    for i, path in enumerate(DEMO_FILE_PATHS, 1):
        assert os.path.exists(path)
        with open(path) as f:
            assert f.read() == f"This is the content of demo file {i}.\n"

def test_merged_file_content():
    import importlib.util
    spec = importlib.util.spec_from_file_location("upload_script", SCRIPT_PATH)
    upload_script = importlib.util.module_from_spec(spec)
    with mock.patch("office365.runtime.auth.authentication_context.AuthenticationContext.acquire_token_for_user", return_value=False):
        spec.loader.exec_module(upload_script)
    merged_content = "".join([f"This is the content of demo file {i}.\n" for i in range(1, 11)])
    with open(MERGED_FILE_PATH) as f:
        assert f.read() == merged_content

def test_sharepoint_upload_mocked():
    import importlib.util
    spec = importlib.util.spec_from_file_location("upload_script", SCRIPT_PATH)
    upload_script = importlib.util.module_from_spec(spec)
    with mock.patch("office365.runtime.auth.authentication_context.AuthenticationContext.acquire_token_for_user", return_value=True), \
         mock.patch("office365.sharepoint.client_context.ClientContext"), \
         mock.patch("builtins.open", mock.mock_open(read_data="data")):
        spec.loader.exec_module(upload_script)
    # If no exception, test passes (actual upload is mocked)
