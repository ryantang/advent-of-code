import unittest

from rucksack import *

class TestingRucksack(unittest.TestCase):
    def test_shared_item(self):
        contents = 'vJrwpWtwJgWrhcsFMMfFFhFp'
        self.assertEqual(Rucksack.shared_items(contents), {"p"})

        contents = 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
        self.assertEqual(Rucksack.shared_items(contents), {"L"})


    def test_total_priority(self):
        rucksacks = [
            'vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
        ]

        self.assertEqual(Rucksack.total_priority(rucksacks), 16 + 38)

    def test_total_priority_from_file(self):
        rucksacks_file = "/Users/ryantang/workspace/advent-of-code/day03_rucksack_reorganization/rucksack_inventory.txt"

        self.assertEqual(Rucksack.total_priority_from_file(rucksacks_file), 157)

if __name__ == '__main__':
    unittest.main()