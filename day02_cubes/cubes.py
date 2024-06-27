class GameVerifier:
    def is_possible(self, shown):
        total_counts = {'green': 13, 'blue': 14, 'red': 12}
        max_shown_by_color = self.max_colors(shown)
        for color, max_shown in max_shown_by_color.items():
            if max_shown > total_counts[color]:
                return False
        return True
    
    def max_colors(self, shown):
        max_counts = {'green': 0, 'blue': 0, 'red': 0}

        game, results = shown.split(':')
        segments = results.split(';')
        for segment in segments:
            color_counts = segment.split(',')
            for color_count in color_counts:
                count, color = color_count.strip().split(' ')
                count = int(count)
                if count > max_counts[color]:
                    max_counts[color] = count
        return max_counts
    
    def power(self, shown):
        max_counts = self.max_colors(shown)
        return max_counts['green'] * max_counts['blue'] * max_counts['red']
    
    def sum_of_power(self, games):
        sum = 0
        for game in games:
            sum += self.power(game)
        return sum
    
    def sum_possible_games(self, games):
        sum = 0
        for game in games:
            if self.is_possible(game):
                game_number = int(game.split(':')[0].split(' ')[1])
                sum += game_number
        return sum
    
    def sum_possible_from_file(self, file):
        f = open(file, 'r')
        lines = f.readlines()
        f.close()

        return self.sum_possible_games(lines)
    
    def sum_of_power_from_file(self, file):
        f = open(file, 'r')
        lines = f.readlines()
        f.close()

        return self.sum_of_power(lines)

