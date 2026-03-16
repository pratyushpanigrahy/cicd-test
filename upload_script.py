import requests
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

# Placeholder link for file upload
PLACEHOLDER_FILE_PATH = "path/to/your/file.txt"  # Replace with your file path
SHAREPOINT_SITE_URL = "https://yourcompany.sharepoint.com/sites/yoursite"  # Replace with your SharePoint site URL
USERNAME = "your-email@yourcompany.com"  # Replace with your SharePoint username
PASSWORD = "your-password"  # Replace with your SharePoint password
SHAREPOINT_LIST_NAME = "YourListName"  # Replace with your SharePoint list name

# Authenticate and connect to SharePoint
ctx_auth = AuthenticationContext(SHAREPOINT_SITE_URL)
if ctx_auth.acquire_token_for_user(USERNAME, PASSWORD):
    ctx = ClientContext(SHAREPOINT_SITE_URL, ctx_auth)
    # Upload file
    with open(PLACEHOLDER_FILE_PATH, 'rb') as file_obj:
        target_folder = ctx.web.lists.get_by_title(SHAREPOINT_LIST_NAME).rootFolder
        name = PLACEHOLDER_FILE_PATH.split("/")[-1]
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
