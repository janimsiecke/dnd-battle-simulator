import json

from simualtor_core.game.sim_logging import LOGGER
from simualtor_core.board.board import Board

def import_board() -> Board:
    try:
        with open('../../data/board_config.json', 'r') as file:
            board_dict = json.load(file)
    except FileNotFoundError:
        LOGGER.error('Unable to find the board configuration file in /data/board_config.json!')

    if not 'board_width' in board_dict.keys() or not 'board_height' in board_dict.keys():
        LOGGER.error('Incorrect configuration data in file /data/board_config.json, missing board_width and/or board_height!')
    return Board(board_dict['board_width'], board_dict['board_height'])