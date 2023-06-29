import pandas as pd
from sqlalchemy import create_engine

from config.dynaconf import settings
from services.logger import logger_debug
from services.sql_queries import execute_sql_query
from constants.sql_queries import INSERT_USER_QUERY, UPDATE_USER_QUERY, GET_USER_QUERY

engine = create_engine(
            'mysql+pymysql://' + settings['DATABASE_UID']+':' + settings['DATABASE_PWD'] + '@' +
            settings['DATABASE_HOST'] + '/' + settings['DATABASE_NAME']
        )


def insert_user(data, id=''):
    fieldnames = ''
    values = ''

    update_sub_query = ""
    for key, value in data.items():
        # insert
        fieldnames += f'{key}, '
        values += f"'{value}', "

        # update
        update_sub_query += f"{key} = '{value}', "

    if id == '':
        logger_debug(f"Inserting user details #{data}")
        query = INSERT_USER_QUERY.format(fieldnames, values)
    else:
        logger_debug(f"Updating user details id #{id}")
        query = UPDATE_USER_QUERY.format(update_sub_query[:-2], id)
    result = execute_sql_query(query)
    return result


def get_user_details(id):
    logger_debug(f"Retrieving user details #{id}")
    result = pd.read_sql_query(GET_USER_QUERY.format(id), engine)
    return result


engine.dispose()
