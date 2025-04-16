"""Helper Func: storage blob"""
import logging
import json
import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient

def read_blob(blob):
    """Func to read blob"""
    try:
        logging.info("Storage helper is running")
        # Set these according to your blob's location
        storage_account_name =  os.environ.get("STG_NAME")
        container_name =  os.environ.get("STG_CONTAINER_NAME")
        blob_name = blob

        # Construct the blob URL
        blob_url = f"https://{storage_account_name}.blob.core.windows.net/{container_name}/{blob_name}"

        # Use DefaultAzureCredential to authenticate via managed identity
        credential = DefaultAzureCredential()

        # Create BlobClient using the managed identity
        blob_client = BlobClient(account_url=f"https://{storage_account_name}.blob.core.windows.net/",
                                 container_name=container_name,
                                 blob_name=blob_name,
                                 credential=credential)

        # Download the blob content
        blob_data = blob_client.download_blob().readall()
        obj = json.loads(blob_data)
        return obj

    except Exception as e:
        logging.error(f"Failed to read blob: {str(e)}")

# def write_blob(): 
   #LOGIC Goes here

# def update_blob():
   # LOGIC Goes here
