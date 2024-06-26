import unittest

from stacker import *

class TestingStacker(unittest.TestCase):
    def test_move(self):
        config0 = [
            ['Z', 'N'],
            ['M', 'C', 'D'],
            ['P'],
        ]
        move1 = 'move 1 from 2 to 1'

        config1 = [
            ['Z', 'N', 'D'],
            ['M', 'C'],
            ['P'],      
        ]

        move2 = 'move 3 from 1 to 3'
        config2 = [
            [],
            ['M', 'C'],
            ['P', 'D', 'N', 'Z'],      
        ]
        
        self.assertEqual(Stacker.move(config0, move1), config1)
        self.assertEqual(Stacker.move(config1, move2), config2)

    def test_mulit_move(self):
        config0 = [
            ['Z', 'N'],
            ['M', 'C', 'D'],
            ['P'],
        ]

        moves = [
            'move 1 from 2 to 1',
            'move 3 from 1 to 3',
            'move 2 from 2 to 1',
            'move 1 from 1 to 2'
        ]

        expected_config = [
            ['C'],
            ['M'],
            ['P', 'D', 'N', 'Z'],
        ]

        self.assertEqual(Stacker.multi_move(config0, moves), expected_config)


    def test_mulit_move_from_file(self):
        moves_file = '/Users/ryan.tang/workspace/advent-of-code/2022/day05_supply_stacks/rearrangement_procedure.txt'

        config0 = [
            ['Z', 'N'],
            ['M', 'C', 'D'],
            ['P'],
        ]

        expected_config = [
            ['C'],
            ['M'],
            ['P', 'D', 'N', 'Z'],
        ]

        self.assertEqual(Stacker.multi_move_from_file(config0, moves_file), expected_config)

    def test_top_crates(self):
        config = [
            ['C'],
            ['M'],
            ['P', 'D', 'N', 'Z'],
        ]

        self.assertEqual(Stacker.top_crates(config), 'CMZ')

    
    def test_together(self):
        moves_file = '/Users/ryan.tang/workspace/advent-of-code/2022/day05_supply_stacks/rearrangement_procedure.txt'

        config0 = [
            ['Z', 'N'],
            ['M', 'C', 'D'],
            ['P'],
        ]

        final_configuration = Stacker.multi_move_from_file(config0, moves_file)
        self.assertEqual(Stacker.top_crates(final_configuration), 'CMZ')

if __name__ == '__main__':
    unittest.main()