import unittest

from gear import *

class TestingSchematic(unittest.TestCase):
    def setUp(self) -> None:
        self.analyzer = SchematicAnalyzer()
        self.schematic_1 =  [ 
            [".", ".", ".", ".", "."],
            [".", "1", "2", "3", "."],
            [".", ".", ".", ".", "."],
        ]

        self.schematic_2 =  [ 
            [".", ".", ".", ".", "."],
            [".", "1", "2", "3", "."],
            [".", ".", "#", ".", "."],
        ]

        self.schematic_5 =  [ 
            ["4", ".", ".", ".", "."],
            [".", "1", "2", "3", "."],
            [".", ".", "#", ".", "."],
        ]

        self.schematic_6 =  [
            ["4", ".", ".", ".", "."],
            [".", "1", ".", "3", "2"],
            ["5", "5", "#", ".", "."],
        ]

        self.schematic_7 =  [ 
            ["4", "@", ".", ".", "."],
            [".", "4", ".", "3", "2"],
            ["5", "5", ".", "!", "."],
        ]

    def test_sum_part_numbers(self):
        self.assertEqual(self.analyzer.sum_part_numbers(self.schematic_1), 0)
        self.assertEqual(self.analyzer.sum_part_numbers(self.schematic_2), 123)
        self.assertEqual(self.analyzer.sum_part_numbers(self.schematic_7), 4+4+32)

    def test_numbers_adjecent_to_symbol(self):
        self.assertEqual(self.analyzer.numbers_adjacent_to_symbol(self.schematic_5), ["123"])
        self.assertEqual(self.analyzer.numbers_adjacent_to_symbol(self.schematic_6), ["1","32", "55"])
        self.assertEqual(self.analyzer.numbers_adjacent_to_symbol(self.schematic_7), ["4", "4", "32"])

    def test_adjacent_coordinates(self):
        last_cell = (2, 3)
        coordinates = [(1, 1), (1, 2)]
        expected = [(0, 0), (0, 1), (0, 2), (0,3), (1, 0), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
        self.assertCountEqual(self.analyzer._adjacent_coordinates(coordinates, last_cell), expected)

        #top and left boundary conditions
        coordinates = [(0, 0)]
        expected = [(0, 1), (1, 0), (1, 1)]
        self.assertCountEqual(self.analyzer._adjacent_coordinates(coordinates, last_cell), expected)

        #bottom and right boundary conditions
        coordinates = [(2, 3)]
        expected = [(1, 3), (1,2), (2, 2)]
        self.assertCountEqual(self.analyzer._adjacent_coordinates(coordinates, last_cell), expected)

    def test_sum_part_numbers_from_file(self):
        file = "/Users/ryan.tang/workspace/advent-of-code/day03_gear/sample.txt"
        self.assertEqual(self.analyzer.sum_part_numbers_from_file(file), 4361)

        file = "/Users/ryan.tang/workspace/advent-of-code/day03_gear/input"
        self.assertEqual(self.analyzer.sum_part_numbers_from_file(file), 553825)

if __name__ == '__main__':
    unittest.main()

