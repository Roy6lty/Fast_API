import logging

logging.basicConfig(filename='fastapi.log',filemode='w',
                    format='%(asctime)s- %(name)s - %(levelname)s -%(message)s',
                    level = logging.DEBUG)
logging.debug('This will be logged')