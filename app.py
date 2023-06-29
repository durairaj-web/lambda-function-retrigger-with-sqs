from services.logger import logger_debug
from controller import user


def hello_lambda(event, context):
    logger_debug(f"EVENT DETAILS: {event}")
    '''
        Input - JSON request { "name": "Julia", "email": "julia@xyz.com", position: "CEO" }
    '''
    return user.process_request(event)
