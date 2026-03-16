import requests
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

# Demo file paths
DEMO_FILE_PATH_1 = "demo_file_1.txt"  # First demo file
DEMO_FILE_PATH_2 = "demo_file_2.txt"  # Second demo file
MERGED_FILE_PATH = "merged_demo_file.txt"  # Merged file
SHAREPOINT_SITE_URL = "https://yourcompany.sharepoint.com/sites/yoursite"  # Replace with your SharePoint site URL
USERNAME = "your-email@yourcompany.com"  # Replace with your SharePoint username
PASSWORD = "your-password"  # Replace with your SharePoint password
SHAREPOINT_LIST_NAME = "YourListName"  # Replace with your SharePoint list name

# Create demo files if they don't exist
for demo_path, content in [
    (DEMO_FILE_PATH_1, "This is the content of demo file 1.\n"),
    (DEMO_FILE_PATH_2, "This is the content of demo file 2.\n")
]:
    try:
        with open(demo_path, 'x') as f:
            f.write(content)
    except FileExistsError:
        pass

# Merge both demo files into one
with open(MERGED_FILE_PATH, 'w') as merged_file:
    for demo_path in [DEMO_FILE_PATH_1, DEMO_FILE_PATH_2]:
        with open(demo_path, 'r') as f:
            merged_file.write(f.read())

# Authenticate and connect to SharePoint
ctx_auth = AuthenticationContext(SHAREPOINT_SITE_URL)
if ctx_auth.acquire_token_for_user(USERNAME, PASSWORD):
    ctx = ClientContext(SHAREPOINT_SITE_URL, ctx_auth)
    # Upload merged file
    with open(MERGED_FILE_PATH, 'rb') as file_obj:
        target_folder = ctx.web.lists.get_by_title(SHAREPOINT_LIST_NAME).rootFolder
        name = MERGED_FILE_PATH
        target_file = target_folder.upload_file(name, file_obj.read())
        ctx.execute_query()
        print(f"File '{name}' uploaded successfully.")
    # Append metadata to SharePoint list
    list_obj = ctx.web.lists.get_by_title(SHAREPOINT_LIST_NAME)
    item_creation_info = {
        'Title': name,
        'FileName': name,
        # Add more fields as needed
    }
    list_obj.add_item(item_creation_info)
    ctx.execute_query()
    print(f"Metadata for '{name}' appended to SharePoint list.")
else:
    print("Authentication failed. Please check your credentials.")
