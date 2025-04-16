import os
import logging
from Helpers.storage_helper import read_blob


def get_name_svc():
    """Module to get the name of employees"""
    logging.info('Get Name Service started..')
    blob_name = os.environ.get("STG_NAME_BLOB")
    try:
        blob_data = read_blob(blob_name)
        #Business LOGIC GOES HERE
        return blob_data
    except Exception as err:
        return {"Error" : err}
