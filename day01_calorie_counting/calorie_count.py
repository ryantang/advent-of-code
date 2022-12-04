class CalorieCounter:

    def __init__(self, calorie_list):
        self.calorie_list = calorie_list

    @classmethod
    def from_file(cls, calorie_file):
        f = open(calorie_file, 'r')
        calorie_list = f.readlines()
        f.close()
        return cls(calorie_list)


    def max_calories(self):
        max_calories = 0
        elf_number = 1
        top_elf = [0, 0]
        
        for item_calories in self.calorie_list:
            if item_calories == "\n":
                elf_number = elf_number + 1
                max_calories = 0
            else:
                max_calories = max_calories + int(item_calories)
                if max_calories > top_elf[1]:
                    top_elf = [elf_number, max_calories]

        return top_elf