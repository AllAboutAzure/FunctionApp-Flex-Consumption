from pydantic import BaseModel
from typing import List

# Define the model
class NameInfo(BaseModel):
    Name: str
    Department: str

# For a list of them
# class NameList(BaseModel):
#     __root__: List[NameInfo]
