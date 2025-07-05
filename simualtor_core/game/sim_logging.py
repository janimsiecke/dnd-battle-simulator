import os
import logging

from datetime import datetime

BATTLE_LOGGER = logging.getLogger('battle_logger')
LOGGER = logging.getLogger('logger')
TURN_COUNTER = 1

def initiate_battle_logging():
    global BATTLE_LOGGER
    if not os.path.isdir('../../log/battle_logs/'):
        os.makedirs('../../log/battle_logs/')
    BATTLE_LOGGER.setLevel(logging.INFO)
    formatter = logging.Formatter(f'%(message)s')
    file_handler = logging.FileHandler(f'../../log/battle_logs/dnd-sim-{datetime.now().strftime("%Y%m%d%H%M%S")}.log')
    file_handler.setFormatter(formatter)
    BATTLE_LOGGER.addHandler(file_handler)

def initiate_logging():
    global LOGGER
    if not os.path.isdir('../../log/'):
        os.makedirs('../../log/')
    LOGGER.setLevel(logging.DEBUG)
    formatter = logging.Formatter(f'[%(levelname)s] {datetime.now().strftime("%d.%m.%Y %H:%M:%S")} - %(message)s')
    file_handler = logging.FileHandler(f'../../log/simulator.log')
    file_handler.setFormatter(formatter)
    LOGGER.addHandler(file_handler)

def log_turn(message: str):
    global BATTLE_LOGGER
    BATTLE_LOGGER.info(f"Turn {TURN_COUNTER} - {message}")

def log_message(message: str):
    global BATTLE_LOGGER
    BATTLE_LOGGER.info(message)

def increase_counter():
    global TURN_COUNTER
    TURN_COUNTER += 1

