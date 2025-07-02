import logging

from datetime import datetime

TURN_COUNTER = 1

def initiate_logging():
    logging.basicConfig(
        filename=f'../../log/dnd-sim-{datetime.now().strftime("%Y%m%d%H%M%S")}.log',
        filemode='a',
        level=logging.DEBUG,
        format=f'%(message)s'
    )

def log_turn(message: str):
    logging.info(f"Turn {TURN_COUNTER} - {message}")

def log_message(message: str):
    logging.info(message)

def increase_counter():
    global TURN_COUNTER
    TURN_COUNTER += 1
