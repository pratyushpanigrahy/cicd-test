import os
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

# Reader Script - Reads merged file and uploads to SharePoint
MERGED_FILE_PATH = "merged_demo_file.txt"
SHAREPOINT_SITE_URL = "https://yourcompany.sharepoint.com/sites/yoursite"
USERNAME = "your-email@yourcompany.com"
PASSWORD = "your-password"
SHAREPOINT_LIST_NAME = "YourListName"

def read_merged_file():
    """Read the merged file and return its content."""
    try:
        with open(MERGED_FILE_PATH, 'r') as f:
            content = f.read()
            print(f"Read merged file: {MERGED_FILE_PATH}")
            return content
    except FileNotFoundError:
        print(f"Merged file not found: {MERGED_FILE_PATH}")
        return None

def upload_to_sharepoint(file_path):
    """Upload file to SharePoint and append metadata."""
    ctx_auth = AuthenticationContext(SHAREPOINT_SITE_URL)
    if ctx_auth.acquire_token_for_user(USERNAME, PASSWORD):
        ctx = ClientContext(SHAREPOINT_SITE_URL, ctx_auth)
        try:
            # Upload file
            with open(file_path, 'rb') as file_obj:
                target_folder = ctx.web.lists.get_by_title(SHAREPOINT_LIST_NAME).rootFolder
                name = os.path.basename(file_path)
                target_file = target_folder.upload_file(name, file_obj.read())
                ctx.execute_query()
                print(f"File '{name}' uploaded successfully.")
            
            # Append metadata to SharePoint list
            list_obj = ctx.web.lists.get_by_title(SHAREPOINT_LIST_NAME)
            item_creation_info = {
                'Title': name,
                'FileName': name,
            }
            list_obj.add_item(item_creation_info)
            ctx.execute_query()
            print(f"Metadata for '{name}' appended to SharePoint list.")
        except Exception as e:
            print(f"Error during SharePoint upload: {e}")
    else:
        print("Authentication failed. Please check your credentials.")

if __name__ == "__main__":
    content = read_merged_file()
    if content:
        print(f"Merged file size: {len(content)} bytes")
        # Uncomment below to upload to SharePoint
        # upload_to_sharepoint(MERGED_FILE_PATH)
