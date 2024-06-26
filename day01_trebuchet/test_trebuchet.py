import unittest

from trebuchet import *

class TestingDecoder(unittest.TestCase):
    def test_decode(self):
        text_line = "1abc2" # first digit is 1, second digit is 2
        self.assertEqual(Decoder.decode(text_line), 12)

        text_line = "pqr3stu8vwx" # first digit is 3, second digit is 8
        self.assertEqual(Decoder.decode(text_line), 38)

        text_line = "a1b2c3d4e5f" # first digit is 3, second digit is 8
        self.assertEqual(Decoder.decode(text_line), 15)

        text_line = "treb7uchet" # first digit is 3, second digit is 8
        self.assertEqual(Decoder.decode(text_line), 77)

    def test_with_file(self):
        file = "/Users/ryan.tang/workspace/advent-of-code/day01_trebuchet/sample.txt"
        self.assertEqual(Decoder.sum_decoded_from_file(file), 142)

        file = "/Users/ryan.tang/workspace/advent-of-code/day01_trebuchet/input"
        self.assertEqual(Decoder.sum_decoded_from_file(file), 54597)

if __name__ == '__main__':
    unittest.main()