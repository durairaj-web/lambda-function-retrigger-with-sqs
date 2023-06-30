from services.logger import logger_debug
from controller import user


# def hello_lambda(event, context):
def hello_lambda():
    event = {
        "Records": [
            {
                "messageId": "5f7c50a8-7a15-4ab4-8d20-db0fa67532ae",
                "body": '{\n "name": "Julia", "email": "julia@xyz.com", "position": "CEO" \n}'
            }
        ]
    }
    logger_debug(f"EVENT DETAILS: {event}")
    '''
        Input - JSON request { "name": "Julia", "email": "julia@xyz.com", "position": "CEO" }
    '''
    return user.process_request(event)


hello_lambda()
