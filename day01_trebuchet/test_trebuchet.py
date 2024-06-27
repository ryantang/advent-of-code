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

        text_line = "treb7uchet" 
        self.assertEqual(Decoder.decode(text_line), 77)

    def test_decode_with_spelling(self):
        text_line = "two1nine" #first digit is 2, second digit is 9
        self.assertEqual(Decoder.decode_with_spelling(text_line), 29)

        text_line = "eightwothree"
        self.assertEqual(Decoder.decode_with_spelling(text_line), 83)

        text_line = "abcone2threexyz"
        self.assertEqual(Decoder.decode_with_spelling(text_line), 13)
 
        text_line = "xtwone3four"
        self.assertEqual(Decoder.decode_with_spelling(text_line), 24)
 
        text_line = "4nineeightseven2" # first digit is 4, second digit is 2
        self.assertEqual(Decoder.decode_with_spelling(text_line), 42)

        text_line = "zoneight234"
        self.assertEqual(Decoder.decode_with_spelling(text_line), 14)
 
        text_line = "7pqrstsixteen"
        self.assertEqual(Decoder.decode_with_spelling(text_line), 76)

        text_line = "twone"
        self.assertEqual(Decoder.decode_with_spelling(text_line), 21)

        text_line = "eightfour2fourvzksqhxmlkpkfktmdzpmthreetwonehv" #need to convert the last "one"
        self.assertEqual(Decoder.decode_with_spelling(text_line), 81)

        text_line = "treb7uchet" 
        self.assertEqual(Decoder.decode(text_line), 77)

    def test_with_file(self):
        file = "/Users/ryan.tang/workspace/advent-of-code/day01_trebuchet/sample.txt"
        self.assertEqual(Decoder.sum_decoded_from_file(file), 142)

        file = "/Users/ryan.tang/workspace/advent-of-code/day01_trebuchet/input"
        self.assertEqual(Decoder.sum_decoded_from_file(file), 54597)

    def test_with_file_and_spelling(self):
        file = "/Users/ryan.tang/workspace/advent-of-code/day01_trebuchet/sample2.txt"
        self.assertEqual(Decoder.sum_decoded_with_spelling_from_file(file), 281)

        file = "/Users/ryan.tang/workspace/advent-of-code/day01_trebuchet/input"
        self.assertEqual(Decoder.sum_decoded_with_spelling_from_file(file), 54504)


if __name__ == '__main__':
    unittest.main()