import unittest

from game_score import *

class TestingGameScore(unittest.TestCase):
    def test_result_score(self):
        win =  (('A','Y'), ('B','Z'), ('C','X'))
        lose = (('A','Z'), ('B','X'), ('C','Y'))
        tie =  (('A','X'), ('B','Y'), ('C','Z'))

        for game in win:
            self.assertEqual(GameScore.result_score(game), 6)
        
        for game in lose:
            self.assertEqual(GameScore.result_score(game), 0)

        for game in tie:
            self.assertEqual(GameScore.result_score(game), 3)

    def test_play_score(self):
        rock = (('A','X'), ('B','X'))
        paper = (('A','Y'), ('C','Y'))
        sciscors = (('A','Z'), ('C','Z'))
        
        for play in rock:
            self.assertEqual(GameScore.play_score(play), 1)
        
        for play in paper:
            self.assertEqual(GameScore.play_score(play), 2)

        for play in sciscors:
            self.assertEqual(GameScore.play_score(play), 3)


    def test_game_score(self):
        self.assertEqual(GameScore.game_score(('A','Y')), 8)
        self.assertEqual(GameScore.game_score(('B','X')), 1)
        self.assertEqual(GameScore.game_score(('C','Z')), 6)

    def test_total_score(self):
        plays = (('A','Y'), ('B','X'), ('C','Z'))
        self.assertEqual(GameScore(plays).total_score(), 15)

    def test_from_file(self):
        game_score = GameScore.from_file('/Users/ryantang/workspace/advent-of-code/day02_rock_paper_scissors/strategy_guide.txt')
        self.assertEqual(game_score.total_score(), 15) 


if __name__ == '__main__':
    unittest.main()
