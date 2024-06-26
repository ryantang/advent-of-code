import re

class Stacker:
    def move(box_config, move) -> list:
        p = re.compile(r'\d+')
        instructions = p.findall(move)

        times = int(instructions[0])
        from_stack = int(instructions[1]) - 1
        to_stack = int(instructions[2]) - 1

        for i in range(times):
            box = box_config[from_stack].pop()

            box_config[to_stack].append(box)
        return box_config

    def multi_move(initial_config, moves) -> list:
        
        current_config = initial_config
        for move in moves:
            current_config = Stacker.move(current_config, move)
    
        return current_config

    def multi_move_from_file(initial_config, moves_file) -> list:
        f = open(moves_file, 'r')
        moves = f.read().splitlines()
        f.close()

        return Stacker.multi_move(initial_config, moves)

    def top_crates(config) -> str:
        top_boxes = ''
        for stack in config:
            top_boxes += stack.pop()
        
        return top_boxes