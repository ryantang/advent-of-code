import string

class Rucksack:

    def shared_items(contents):
        num_items = len(contents)
        midpoint = int(num_items/2)

        compartment1 = set(contents[:midpoint])
        compartment2 = set(contents[midpoint:])

        return compartment1.intersection(compartment2)

    def total_priority(rucksacks):
        total_score = 0
        for contents in rucksacks:
            shared_item = next(iter(Rucksack.shared_items(contents)))
            total_score = total_score + Rucksack.priority_scores(shared_item)

        return total_score


    def total_priority_from_file(inventory_file):
        f = open(inventory_file, 'r')
        rucksacks = f.read().splitlines()
        f.close()

        return Rucksack.total_priority(rucksacks)

    def find_badge(three_rucksacks):
        elf1 = set(three_rucksacks[0])
        elf2 = set(three_rucksacks[1])
        elf3 = set(three_rucksacks[2])

        return set.intersection(elf1, elf2, elf3)


    def badge_total_priority(rucksacks):
        if len(rucksacks) % 3 != 0:
            raise Exception("Danger! Elves must go in groups of three.")

        total_priority = 0
        for i in range(0, int(len(rucksacks)), 3):
            three_rucksacks = rucksacks[i:i+3]
            badge = next(iter(Rucksack.find_badge(three_rucksacks)))
            total_priority = total_priority + Rucksack.priority_scores(badge)
        
        return total_priority

    def badge_priority_from_file(inventory_file):
        f = open(inventory_file, 'r')
        rucksacks = f.read().splitlines()
        f.close()

        return Rucksack.badge_total_priority(rucksacks)

    def priority_scores(item):
        scores = {}
        for i in range(52):
            scores.update({string.ascii_letters[i]: i+1})

        return scores[item]