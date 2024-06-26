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


    def test_find_badge(self):
        rucksacks = [
            'vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg'
        ]

        self.assertEqual(Rucksack.find_badge(rucksacks), {'r'})

        rucksacks = [
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw'
        ]

        self.assertEqual(Rucksack.find_badge(rucksacks), {'Z'})

    def test_badge_priorities(self):
        rucksacks = [
            'vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw'
        ]

        self.assertEqual(Rucksack.badge_total_priority(rucksacks), 18 + 52)

    def test_badge_priorities_error(self):
        wrong_number_of_rucksacks = [       #must be multiples of threes
            'vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT'
        ]

        with self.assertRaises(Exception):
            Rucksack.badge_total_priority(wrong_number_of_rucksacks)

    
    def test_badge_priority_from_file(self):
        rucksacks_file = "/Users/ryantang/workspace/advent-of-code/day03_rucksack_reorganization/rucksack_inventory.txt"

        self.assertEqual(Rucksack.badge_priority_from_file(rucksacks_file), 70)

if __name__ == '__main__':
    unittest.main()