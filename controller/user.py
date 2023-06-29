import copy
import json
from datetime import datetime, timedelta

from config.dynaconf import settings
from services.logger import logger_debug, logger_error
from constants import exception, messages
from services.utils import insert_user


def process_request(event):
    batch_item_failures = []
    sqs_batch_response = {}
    for record in event['Records']:
        try:
            handle_request(json.loads(record['body']))
        except Exception as e:
            logger_error(e)
            batch_item_failures.append({"itemIdentifier": record['messageId']})
    sqs_batch_response["batchItemFailures"] = batch_item_failures
    return sqs_batch_response


def handle_request(data):
    try:
        if data is not None:
            logger_debug(f"Input data - {data}")
            try:
                # Inserting User
                inserted_id = insert_user(data)
                msg = copy.deepcopy(messages.VALID_RESPONSE)
                logger_debug(msg.replace("{INSERTED_ID}", str(inserted_id)))
            except Exception as e:
                logger_error(e)
                raise Exception(messages.INVALID_RESPONSE)
        else:
            logger_error(copy.deepcopy(exception.EMPTY_DATA_EXCEPTION))
            raise Exception(exception.EMPTY_DATA_EXCEPTION)
    except Exception as e:
        logger_error(e)
        raise Exception(exception.UNHANDLED_EXCEPTION)
