"""Helper Func: Keyvault secrets"""
import os
import logging
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def read_secrets(secrets):
    """Func to read secrets"""
    try:
        logging.info("Keyvault helper is running")
        # Replace with your Key Vault name and secret name
        key_vault_name = os.environ.get("KEY_VAULT_NAME")
        secret_names = secrets

        # Construct the Key Vault URI
        kv_uri = f"https://{key_vault_name}.vault.azure.net"

        # Use DefaultAzureCredential (automatically picks up managed identity in Azure)
        credential = DefaultAzureCredential()

        # Create the SecretClient
        secret_client = SecretClient(vault_url=kv_uri, credential=credential)

        retrieved_secrets = []
        # Get the secret value
        for secret in secret_names:
            retrieved_secrets.append({secret : secret_client.get_secret(secret)})

        return retrieved_secrets

    except Exception as e:
        logging.error(f"Error reading secret: {str(e)}")


# def update_secrets():
   # LOGIC Goes here