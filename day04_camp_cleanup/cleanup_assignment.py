class CleanupAssignment:

    def __init__(self, assignments):
        self.assignments = assignments

    @classmethod
    def from_file(cls, assignment_file):
        f = open(assignment_file, 'r')
        line = f.readline()
        assignment_tuples = []
        while line:
            parts = line.split(',')
            assignment_tuples.append((parts[0],parts[1]))
            line = f.readline()
        f.close()
        
        return cls(assignment_tuples)

    def fully_contains(assignment):
        elf1_sections, elf2_sections = CleanupAssignment.map_sections(assignment)

        if elf1_sections.issubset(elf2_sections):
            return True
        elif elf2_sections.issubset(elf1_sections):
            return True
        else:
            return False

    def number_of_contains(self):
        count = 0
        for i in self.assignments:
            if CleanupAssignment.fully_contains(i):
                count += 1
        
        return count

    def overlaps(assignment):
        elf1_sections, elf2_sections = CleanupAssignment.map_sections(assignment)

        if len(set.intersection(elf1_sections, elf2_sections)) == 0:
            return False
        else:
            return True

    def number_of_overlaps(self):
        count = 0
        for i in self.assignments:
            if CleanupAssignment.overlaps(i):
                count += 1
        
        return count

    def map_sections(assignment):
        elf1_assignment = assignment[0].split('-')
        elf1_sections = set(range(int(elf1_assignment[0]),int(elf1_assignment[1])+1))
        
        elf2_assignment = assignment[1].split('-')
        elf2_sections = set(range(int(elf2_assignment[0]),int(elf2_assignment[1])+1))

        return elf1_sections,elf2_sections