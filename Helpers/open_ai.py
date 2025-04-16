"""Helper Func: Open AI"""
import os
import logging
from openai import OpenAI
from typing import Union, List

# Azure OpenAI Configuration
AZURE_OPENAI_CONFIG = {
    "api_key": os.environ["OPENAI_KEY"], # open ai key
    "api_base": os.environ["OPENAI_URL"], # your azure open ai resource 
    "api_version": "2023-12-01-preview",  # Use the version that matches your deployment
    "deployment_name": "gpt-4-embedding",  # e.g. gpt-4-embedding etc.
}

# Create a client using Azure OpenAI
def create_azure_openai_client(config: dict) -> OpenAI:
    client = OpenAI(
        api_key=config["api_key"],
        base_url=f"{config['api_base']}/openai/deployments/{config['deployment_name']}",
        default_headers={"api-key": config["api_key"]},
        api_version=config["api_version"]
    )
    return client

# Function to get embeddings
def get_embeddings(input_text: Union[str, List[str]]) -> List[List[float]]:
    logging.info("Open AI helper is running")
    if isinstance(input_text, str):
        input_text = [input_text]

    client = create_azure_openai_client(AZURE_OPENAI_CONFIG)

    try:
        response = client.embeddings.create(input=input_text, model=AZURE_OPENAI_CONFIG["deployment_name"])
        embeddings = [item.embedding for item in response.data]
        return embeddings
    except Exception as e:
        print(f"Error getting embeddings: {e}")
        return []

# # Example usage
# if __name__ == "__main__":
#     result = get_embeddings("Hello world from Azure OpenAI")
#     print(result[0][:5])  # Show first 5 values of the embedding
