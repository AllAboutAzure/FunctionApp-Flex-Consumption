import azure.functions as func

from Controller import app as fastapi_app

# With Fast API Wrapper 

app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)


##########################################################################################
#******************* NORMAL FUNCTION APP CODE ************************
# app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


# @app.route(route="get_company",methods=["GET"])
# def get_company(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('GET Company Details')
#     company_details = get_company_svc()
#     if company_details:
#         return func.HttpResponse(f"The Company Details are :: {company_details}")
#     else:
#         return func.HttpResponse(
#              "The api fetch failed",
#              status_code=500
#         )
    
# @app.route(route="get_name",methods=["GET"])
# def get_name(req: func.HttpRequest) -> func.HttpResponse: #req: func.HttpRequest -- filtering if required.
#     logging.info('GET Names')
#     names = get_name_svc()
#     if names:
#         return func.HttpResponse(f"The Name Details are :: {names}")
#     else:
#         return func.HttpResponse(
#              "The api fetch failed",
#              status_code=500
#         )
################################################################################################
