class CalorieCount:
    def most_calories(file):
        f = open(file, 'r')
        all_lines = f.readlines()
        f.close()
        return CalorieCount.max_calories(all_lines)


    def max_calories(calorie_list):
        max_calories = 0
        elf_number = 1
        top_elf = [0, 0]
        
        for item_calories in calorie_list:
            if item_calories == "\n":
                elf_number = elf_number + 1
                max_calories = 0
            else:
                max_calories = max_calories + int(item_calories)
                if max_calories > top_elf[1]:
                    top_elf = [elf_number, max_calories]

        return top_elf