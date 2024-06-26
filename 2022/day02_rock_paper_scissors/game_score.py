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
        scoring = {
            ('A','Y'): 6,
            ('B','Z'): 6,
            ('C','X'): 6,
            ('A','Z'): 0, 
            ('B','X'): 0, 
            ('C','Y'): 0,
            ('A','X'): 3, 
            ('B','Y'): 3, 
            ('C','Z'): 3,
        }
        return(scoring[plays])

    def play_score(plays):
        scoring = {'X': 1, 'Y': 2, 'Z': 3}
        return(scoring[plays[1]])
    
    def game_score(plays):
        return(GameScore.result_score(plays) + GameScore.play_score(plays))

    def total_score(self):
        score_counter = 0
        for play in self.plays:
            score_counter = score_counter + GameScore.game_score(play)
        
        return score_counter