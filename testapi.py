import uvicorn
from src import api_routes
from src import Nested_body
from src import Declare_request_Example
from src import Response_model
from src import Formfields
from src import Request_Files
from src import Handling_Errors
from src import Path_operation
from src import Json_encoders
from src import fast_dependencies
from src import security
from src import JWT_token
from sql_app import main_sql
from sub_app import main_subapp


from src.api_routes import students

if __name__ == '__main__':
    uvicorn.run('src:app', port=8000,log_level='info', reload=True)

