import fastapi
import json
from typing import List
from Services.company_svc import get_company_svc
from Services.name_svc import get_name_svc
# from Helpers.keyvault_helper import read_secrets
from Models.Company import CompanyInfo
from Models.Name import NameInfo


app = fastapi.FastAPI(
   title="Project Pilot",
    description="This is Pilot setup",
    version="1.0.1",
     contact={
        "name": "DevOpsWithYoge",
        "url": "https://medium.com/@devopswithyoge",
        "email": "devopswithyoge@github.com",
    }
   )


################# Company Details #######################
@app.get("/get_company_details",tags=["Company Details"],response_model=List[CompanyInfo])
async def get_company_details():
    company_details = get_company_svc()
    return company_details # json.load()

@app.post("/post_company_details/", tags=["Company Details"])
async def create_company_details(details: List[CompanyInfo]):
    # if item_id in items_db: #TODO: If needed you can check for the validation
    #     raise HTTPException(status_code=400, detail="Item already exists")
    return {"message": "Details Added to the Storage", "item": details}

@app.put("/update_company_name/{company_name}", tags=["Company Details"])
async def update_company_details(company_name: str):
    # if item_id in items_db: #TODO: If needed you can check for the validation
    #     raise HTTPException(status_code=400, detail="Item already exists")
    return {"message": "Details Updated to the Storage", "item": company_name}

@app.delete("/delete_company_details/", tags=["Company Details"])
async def delete_company_details(details: List[CompanyInfo]):
    # if item_id in items_db: #TODO: If needed you can check for the validation
    #     raise HTTPException(status_code=400, detail="Item already exists")
    return {"message": "Details deleted to the Storage", "item": details}


################# Name Details ###############################
@app.get("/get_names",tags=["Name Details"],response_model=List[NameInfo]) #@app.get("/hello/{name}") with parameters 
async def get_names():
    names = get_name_svc()
    return names
