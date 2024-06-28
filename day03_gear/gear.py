import string

class SchematicAnalyzer:
    def sum_part_numbers(self, schematic):
        result = 0
        for i in self.numbers_adjacent_to_symbol(schematic):
            result += int(i)
        return result
    
    def sum_part_numbers_from_file(self, file):
        f = open(file, 'r')
        lines = f.readlines()
        f.close()

        #convert lines to 2D array
        schematic = []
        for line in lines:
            schematic.append(list(line.strip()))

        return self.sum_part_numbers(schematic)

    def numbers_adjacent_to_symbol(self, schematic):
        numbers = []
        coordinates = []

        for i in range(len(schematic)):
            digit_parts = []
            for j in range(len(schematic[i])):
                if schematic[i][j].isdigit():
                    digit_parts.append(schematic[i][j])
                    coordinates.append((i,j))
                else:
                    self._append_if_adjecent_to_symbol(digit_parts, coordinates, schematic, numbers)
            self._append_if_adjecent_to_symbol(digit_parts, coordinates, schematic, numbers)
        return numbers
    
    def _append_if_adjecent_to_symbol(self, digit_parts, coordinates, schematic, numbers):
        if digit_parts:
            if self._is_adjacent_to_symbol(coordinates, schematic):
                numbers.append("".join(digit_parts))
            digit_parts.clear()
            coordinates.clear()
    
    def _is_adjacent_to_symbol(self, coordinates, schematic):
        last_cell = (len(schematic) - 1, len(schematic[-1]) - 1)
        for coordinate in self._adjacent_coordinates(coordinates, last_cell):
            if self._is_symbol(schematic[coordinate[0]][coordinate[1]]):
                return True
    
    def _is_symbol(self, char):
        valid_symbols = string.punctuation.replace('.', '')
        return char in valid_symbols

    def _adjacent_coordinates(self, coordinates, last_cell):
        adjacent = []
        for coordinate in coordinates:
            row, col = coordinate
            if row > 0: 
                adjacent.append((row - 1, col)) #above
            if row < last_cell[0]:
                adjacent.append((row + 1, col)) #below

        if coordinates[0][1] > 0: #first coordinate isn't on the left boundary
            adjacent.append((coordinates[0][0], coordinates[0][1] - 1)) #left
            if row > 0:
                adjacent.append((coordinates[0][0] - 1, coordinates[0][1] - 1)) #diagonal up left
            if row < last_cell[0]:
                adjacent.append((coordinates[0][0] + 1, coordinates[0][1] - 1)) #diagonal down left

        if coordinates[-1][1] < last_cell[1]: #last coordinate isn't on the right boundary
            adjacent.append((coordinates[-1][0], coordinates[-1][1] + 1)) #right
            if row > 0:
                adjacent.append((coordinates[-1][0] - 1, coordinates[-1][1] + 1)) #diagonal up right
            if row < last_cell[0]:
                adjacent.append((coordinates[-1][0] + 1, coordinates[-1][1] + 1)) #diagonal down right
        return adjacent