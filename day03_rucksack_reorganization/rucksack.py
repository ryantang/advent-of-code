import string

class Rucksack:

    def shared_items(contents):
        num_items = len(contents)
        midpoint = int(num_items/2)

        compartment1 = set(contents[:midpoint])
        compartment2 = set(contents[midpoint:])

        return compartment1.intersection(compartment2)

    def total_priority(rucksacks):
        priority_scores = {}
        for i in range(52):
            priority_scores.update({string.ascii_letters[i]: i+1})

        total_score = 0
        for contents in rucksacks:
            shared_item = next(iter(Rucksack.shared_items(contents)))
            total_score = total_score + priority_scores[shared_item]

        return total_score


    def total_priority_from_file(inventory_file):
        f = open(inventory_file, 'r')
        rucksacks = f.readlines()
        f.close()

        return Rucksack.total_priority(rucksacks)
