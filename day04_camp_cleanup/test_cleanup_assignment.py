import unittest

from cleanup_assignment import *

class TestingCleanupAssignment(unittest.TestCase):
    def test_fully_contains(self):
        assignment = ('2-4', '6-8')
        self.assertEqual(CleanupAssignment.fully_contains(assignment), False)


        assignment = ('2-8', '3-7')
        self.assertEqual(CleanupAssignment.fully_contains(assignment), True)

    def test_number_of_contains(self):
        assignments = [
            ('2-4', '6-8'),
            ('2-8', '3-7'),
        ]

        cleanup_assignment = CleanupAssignment(assignments)
        self.assertEqual(cleanup_assignment.number_of_contains(), 1)

    def test_from_file(self):
        assignment_file = '/Users/ryantang/workspace/advent-of-code/day04_camp_cleanup/assignments.txt'

        cleanup_assignment = CleanupAssignment.from_file(assignment_file)
        self.assertEqual(cleanup_assignment.number_of_contains(), 2)

if __name__ == '__main__':
    unittest.main()