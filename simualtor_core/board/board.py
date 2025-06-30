from enum import Enum
from pprint import pprint

from simualtor_core.actors.base_actor import Actor

class BoardMarkers(Enum):
    OCCUPIED = 'X'

class Board:
    boundaries: (int, int)
    board: dict
    actors: dict

    def __init__(self, width: int = 1, height: int = 1):
        self.boundaries = (width, height)
        self.board = {}
        self.actors = {}

    def __check_empty(self, coord: (int, int)) -> bool:
        return coord not in self.board.keys()

    def __check_out_of_bounds(self, pos: (int, int)):
        return pos[0] < 0 or pos[1] < 0 or pos[0] > self.boundaries[0] or pos[1] > self.boundaries[1]

    def add_obstacle(self, name: str, pos: (int, int)):
        if self.__check_empty(pos) and not self.__check_out_of_bounds(pos):
            if name is None:
                name = BoardMarkers.OCCUPIED.value
            self.board[pos] = name

    def remove_obstacle(self, pos: (int, int)):
        try:
            self.board.pop(pos)
        except KeyError:
            pass

    def add_actor(self, name: str, actor: Actor, pos: (int, int)):
        if self.__check_empty(pos) and name not in self.actors.keys() and not self.__check_out_of_bounds(pos):
            self.actors[name] = actor
            self.board[pos] = name

    def remove_actor(self, name: str):
        try:
            self.actors.pop(name)
        except KeyError:
            pass
        for key, value in self.board.items():
            if value is name:
                self.board.pop(key)
                break

    def move_actor(self, name: str, end_pos: (int, int)):
        if self.__check_empty(end_pos) and not self.__check_out_of_bounds(end_pos):
            for key, value in self.board.items():
                if value is name:
                    self.board.pop(key)
                    break
            self.board[end_pos] = name

    @staticmethod
    def calculate_distance(start: (int, int), end: (int, int)) -> int:
        return  max(abs(end[0] - start[0]), abs(end[1] - start[1])) * 5

    def present_board(self):
        pprint(self.board)