import uvicorn
from src import api_routes
from src import Nested_body
from src import Declare_request_Example
from src import Response_model
from src import Formfields
from src import Request_Files

from src.api_routes import students

if __name__ == '__main__':
    uvicorn.run('src:app', port=8000,log_level='info', reload=True)

