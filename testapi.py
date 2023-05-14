import uvicorn
import api_routes
from api_routes import students

if __name__ == '__main__':
    uvicorn.run('__init__:app', port=8000,log_level='info', reload=True)

