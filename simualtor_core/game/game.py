import json

from simualtor_core.game.sim_logging import LOGGER
from simualtor_core.importer.import_board import import_board
from simualtor_core.importer.import_creature import import_creature
from simualtor_core.actors.base_actor import Actor
from simualtor_core.board.board import Board

class Game:
    board: Board
    players: {}
    allies: {}
    enemies: {}
    def __init__(self):
        self.__get_board()
        self.__get_actors()
        self.__populate_board()
        self.board.present_board()
        self.board.move_actor('Wolf A', (3, 2))
        self.board.present_board()

    def __get_board(self):
        self.board = import_board()
        LOGGER.debug(f'Board created with dimensions {self.board.boundaries[0]}x{self.board.boundaries[1]}')

    def __populate_board(self):
        with open('../../data/board_config.json', 'r') as file:
            board_dict = json.load(file)
        if board_dict['board_impassable']:
            for coordinates in board_dict['board_impassable']:
                self.board.add_obstacle(None, coordinates)
            LOGGER.debug(f'Added obstacles at:{board_dict['board_impassable']}')
        if board_dict['board_player_placement']:
            for entry in board_dict['board_player_placement']:
                if entry[0] in self.players.keys():
                    if self.board.add_actor(entry[0], entry[1]):
                        LOGGER.debug(f'Placed {entry[0]} at {entry[1]}')
                    else:
                        LOGGER.warning(f'Unable to place {entry[0]} at {entry[1]}')
        if board_dict['board_ally_placement']:
            for entry in board_dict['board_ally_placement']:
                if entry[0] in self.allies.keys():
                    if self.board.add_actor(entry[0], entry[1]):
                        LOGGER.debug(f'Placed {entry[0]} at {entry[1]}')
                    else:
                        LOGGER.warning(f'Unable to place {entry[0]} at {entry[1]}')
        if board_dict['board_enemy_placement']:
            for entry in board_dict['board_enemy_placement']:
                if entry[0] in self.enemies.keys():
                    if self.board.add_actor(entry[0], entry[1]):
                        LOGGER.debug(f'Placed {entry[0]} at {entry[1]}')
                    else:
                        LOGGER.warning(f'Unable to place {entry[0]} at {entry[1]}')

    def __get_actors(self):
        self.players = {}
        self.allies = {}
        self.enemies = {}
        ally_list = import_creature('../../data/allies.json')
        for ally in ally_list:
            self.allies[ally[0]] = ally[1]
        LOGGER.debug(f'Allies imported: {self.allies}')
        enemy_list = import_creature('../../data/enemies.json')
        for enemy in enemy_list:
            self.enemies[enemy[0]] = enemy[1]
        LOGGER.debug(f'Enemies imported: {self.enemies}')