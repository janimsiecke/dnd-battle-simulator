import unittest

from simualtor_core.board import board
from simualtor_core.actors import base_actor

class TestBoard(unittest.TestCase):
    test_board = board.Board(25, 25)
    test_actor = base_actor.Actor("Bort")

    def test_calculate_distance(self):
        self.assertEqual(board.Board.calculate_distance((3, 3), (5, 4)), 10)
        self.assertEqual(board.Board.calculate_distance((3, 3), (5, 1)), 10)
        self.assertEqual(board.Board.calculate_distance((3, 3), (0, 6)), 15)
        self.assertEqual(board.Board.calculate_distance((3, 3), (5, 3)), 10)

    def test_add_actor(self):
        compare_board = {(5, 5): 'Bort'}
        compare_actors = {"Bort": self.test_actor}
        self.test_board.add_actor("Bort", self.test_actor, (5, 5))
        self.assertEqual(self.test_board.board, compare_board)
        self.assertEqual(self.test_board.actors, compare_actors)
        self.test_board.add_actor("Bort", self.test_actor, (5, 5))
        self.assertEqual(self.test_board.board, compare_board)
        self.assertEqual(self.test_board.actors, compare_actors)
        self.test_board.add_actor("Bart", self.test_actor, (30, 30))
        self.assertEqual(self.test_board.board, compare_board)
        self.assertEqual(self.test_board.actors, compare_actors)
        self.test_board.add_actor("Bart", self.test_actor, (-5, 30))
        self.assertEqual(self.test_board.board, compare_board)
        self.assertEqual(self.test_board.actors, compare_actors)

    def test_move_actor(self):
        compare_board = {(10, 5): 'Bort'}
        self.test_board.move_actor("Bort", (10, 5))
        self.assertEqual(self.test_board.board, compare_board)
        self.test_board.move_actor("Bort", (-5, 5))
        self.assertEqual(self.test_board.board, compare_board)
        self.test_board.move_actor("Bort", (30, 5))
        self.assertEqual(self.test_board.board, compare_board)

    def test_remove_actor(self):
        compare_board = {(10, 5): 'Bort'}
        self.test_board.remove_actor("Bart")
        self.assertEqual(self.test_board.board, compare_board)
        compare_board = {}
        self.test_board.remove_actor("Bort")
        self.assertEqual(self.test_board.board, compare_board)