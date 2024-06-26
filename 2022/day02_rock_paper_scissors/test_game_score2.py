import unittest

from game_score2 import *

class TestingGameScore(unittest.TestCase):
    def test_result_score(self):
        win =  (('A','Z'), ('B','Z'), ('C','Z'))
        lose = (('A','X'), ('B','X'), ('C','X'))
        tie =  (('A','Y'), ('B','Y'), ('C','Y'))

        for game in win:
            self.assertEqual(GameScore.result_score(game), 6)
        
        for game in lose:
            self.assertEqual(GameScore.result_score(game), 0)

        for game in tie:
            self.assertEqual(GameScore.result_score(game), 3)

    def test_play_score(self):
        rock = (('A','Y'), ('B','X'), ('C','Z'))
        paper = (('A','Z'), ('B','Y'), ('C','X'))
        sciscors = (('A','X'), ('B','Z'),('C','Y'))
        
        for play in rock:
            self.assertEqual(GameScore.play_score(play), 1)
        
        for play in paper:
            self.assertEqual(GameScore.play_score(play), 2)

        for play in sciscors:
            self.assertEqual(GameScore.play_score(play), 3)


    def test_game_score(self):
        self.assertEqual(GameScore.game_score(('A','Y')), 4)
        self.assertEqual(GameScore.game_score(('B','X')), 1)
        self.assertEqual(GameScore.game_score(('C','Z')), 7)

    def test_total_score(self):
        plays = (('A','Y'), ('B','X'), ('C','Z'))
        self.assertEqual(GameScore(plays).total_score(), 12)

    def test_from_file(self):
        game_score = GameScore.from_file('/Users/ryantang/workspace/advent-of-code/day02_rock_paper_scissors/strategy_guide.txt')
        self.assertEqual(game_score.total_score(), 12) 


if __name__ == '__main__':
    unittest.main()
