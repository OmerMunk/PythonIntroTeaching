import logging
import datetime

def log_error(data):
    logging.error(f'{datetime.datetime.now()}: {data}')

def log(data):
    logging.info(f'{datetime.datetime.now()}: {data}')