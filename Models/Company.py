from pydantic import BaseModel
from typing import List

# Define the model
class CompanyInfo(BaseModel):
    Company: str
    Place: str
