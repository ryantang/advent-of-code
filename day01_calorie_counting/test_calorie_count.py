import unittest

from calorie_count import *

class TestingCalorieCount(unittest.TestCase):

    def test_most_calories(self):
        self.assertEqual(CalorieCount.most_calories("/Users/ryantang/workspace/advent-of-code/day01_calorie_counting/calorie_log.txt"), [4, 24000])

    def test_max_calories(self):
        calorie_list = ['1\n', '2\n', '3\n'] # one elf with 6 total calories
        self.assertEqual(CalorieCount.max_calories(calorie_list), [1,6])

        calorie_list = ['1\n', '2\n', '3\n', '\n', '6\n', '7\n'] # two elves: first with 6 calories and second with 13 calories
        self.assertEqual(CalorieCount.max_calories(calorie_list), [2,13])


if __name__ == '__main__':
    unittest.main()