import heapq
class CalorieCounter:

    def __init__(self, calorie_list):
        self.calorie_list = calorie_list

    @classmethod
    def from_file(cls, calorie_file):
        f = open(calorie_file, 'r')
        calorie_list = f.readlines()
        f.close()
        return cls(calorie_list)

    def total_cal_by_elf(self):
        i = 0
        elf = [0]
        
        for item_calories in self.calorie_list:
            if item_calories == "\n":
                i = i + 1
                elf.append(0)
            else:
                elf[i] = elf[i] + int(item_calories)

        return elf

    def max_calories(self):
        return(max(self.total_cal_by_elf()))
    
    def sum_top3_calories(self):
        top3 = heapq.nlargest(3,self.total_cal_by_elf())
        return(sum(top3))