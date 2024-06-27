import unittest

from cubes import *
class TestGameVerifier(unittest.TestCase):

    def setUp(self):
        self.verifier = GameVerifier()
        self.sample_games = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            ]

    def test_is_possible(self):
        shown = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        self.assertEqual(self.verifier.is_possible(shown), True)

        shown = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        self.assertEqual(self.verifier.is_possible(shown), False)

    def test_max_colors(self):
        shown = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        expected = {"blue": 6, "red": 4,"green": 2}
        self.assertEqual(self.verifier.max_colors(shown), expected)

        shown = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        expected = {"blue": 6, "red": 20,"green": 13}
        self.assertEqual(self.verifier.max_colors(shown), expected)

    def test_power(self):
        shown = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        self.assertEqual(self.verifier.power(shown), 48)

        shown = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        self.assertEqual(self.verifier.power(shown), 1560)

    def test_sum_of_power(self):
        self.assertEqual(self.verifier.sum_of_power(self.sample_games), 2286)

    def test_sum_possible_games(self):
        self.assertEqual(self.verifier.sum_possible_games(self.sample_games), 8)

    def test_sum_possible_from_file(self):
        file = "/Users/ryan.tang/workspace/advent-of-code/day02_cubes/sample.txt"
        self.assertEqual(self.verifier.sum_possible_from_file(file), 8)

        file = "/Users/ryan.tang/workspace/advent-of-code/day02_cubes/input"
        self.assertEqual(self.verifier.sum_possible_from_file(file), 2541)

    def test_sum_of_power_from_file(self):
        file = "/Users/ryan.tang/workspace/advent-of-code/day02_cubes/sample.txt"
        self.assertEqual(self.verifier.sum_of_power_from_file(file), 2286)

        file = "/Users/ryan.tang/workspace/advent-of-code/day02_cubes/input"
        self.assertEqual(self.verifier.sum_of_power_from_file(file), 66016)

if __name__ == '__main__':
    unittest.main()