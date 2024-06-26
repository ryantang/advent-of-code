import unittest

from calorie_count import *

class TestingCalorieCount(unittest.TestCase):
    def test_max_calories(self):
        calorie_list = ['1\n', '2\n', '3\n'] # one elf with 6 total calories
        calorie_counter = CalorieCounter(calorie_list)
        self.assertEqual(calorie_counter.max_calories(), 6)

        calorie_list = ['1\n', '2\n', '3\n', '\n', '8\n', '7\n'] # two elves: first with 6 calories and second with 15 calories
        calorie_counter = CalorieCounter(calorie_list)
        self.assertEqual(calorie_counter.max_calories(), 15)


    def test_total_cal_by_elf(self):
        calorie_list = ['1\n', '2\n', '3\n', '\n', '6\n', '7\n'] # two elves: first with 6 calories and second with 13 calories
        calorie_counter = CalorieCounter(calorie_list)
        self.assertEqual(calorie_counter.total_cal_by_elf(), [6, 13])


    def test_sum_top3_cal_by_elf(self):
        calorie_list = ['1\n', '2\n', '\n', '6\n', '7\n', '\n', '32\n', '\n', '2\n']
        calorie_counter = CalorieCounter(calorie_list)
        self.assertEqual(calorie_counter.sum_top3_calories(), 48) # 32 (elf 4) + 15 (elf 2) + 3 (elf1)

    def test_with_file(self):
        calorie_counter = CalorieCounter.from_file("/Users/ryantang/workspace/advent-of-code/day01_calorie_counting/calorie_log.txt")
        self.assertEqual(calorie_counter.max_calories(), 24000)

if __name__ == '__main__':
    unittest.main()