class GameScore:
    def __init__(self, plays):
        self.plays = plays

    @classmethod
    def from_file(cls, plays_file):
        plays = []
        f = open(plays_file, 'r')
        line = f.readline()
        while(line):
            play = tuple(line.split())
            plays.append(play)
            line = f.readline()
        f.close()
        
        return cls(plays)

    def result_score(plays):
        scoring = {'X': 0, 'Y': 3, 'Z': 6}
        return(scoring[plays[1]])

    def play_score(plays):
        scoring = {
            ('A','Y'): 1, 
            ('B','X'): 1, 
            ('C','Z'): 1,
            ('A','Z'): 2, 
            ('B','Y'): 2,
            ('C','X'): 2,
            ('A','X'): 3,
            ('B','Z'): 3,
            ('C','Y'): 3,
        }
        return(scoring[plays])
    
    def game_score(plays):
        return(GameScore.result_score(plays) + GameScore.play_score(plays))

    def total_score(self):
        score_counter = 0
        for play in self.plays:
            score_counter = score_counter + GameScore.game_score(play)
        
        return score_counter