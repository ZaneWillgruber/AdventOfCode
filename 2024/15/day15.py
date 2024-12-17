import re

def main():
    part1()
    part2()

def part1():
    output = parseFile()
    tile_map = output['map']
    directions = output['directions']
    running_total = 0

    for direction in directions:
        able_to_move, amount = can_move(tile_map, tile_map['@'][0], direction)
        if able_to_move:
            move_all(tile_map, tile_map['@'][0], amount, direction)


    for box in tile_map['O']:
        running_total = running_total + (100 * box[1] + box[0])

    print(f'Part 1: {running_total}')
    
def part2():
    return

def can_move(map, current_position, direction):
    attempt_position = get_next_position(current_position, direction)
    move_counter = 0

    while not attempt_position in map['#']:
        if attempt_position in map['O']:
            attempt_position = get_next_position(attempt_position, direction)
            move_counter += 1
        else:
            move_counter += 1
            return True, move_counter

    return False, move_counter

def move_all(map, current_position, amount, direction):
    for i in range(amount):
        next_position = get_next_position(current_position, direction)
        if i == 0:
            map['@'][0] = next_position
            current_position = next_position
        else:
            index = map['O'].index(current_position)
            next_position = get_next_position(current_position, direction)
            map['O'][index] = next_position
            current_position = next_position

def get_next_position(current_position, direction):
    direction_tuple = (0, 0)
    if direction == '<':
        direction_tuple = (-1, 0)
    elif direction == '>':
        direction_tuple = (1, 0)
    elif direction == '^':
        direction_tuple = (0, -1)
    else:
        direction_tuple = (0, 1)

    return (current_position[0] + direction_tuple[0], current_position[1] + direction_tuple[1])

def parseFile():
    output = {
        'map': {
            '@': [],
            '#': [],
            'O': [],
        },
        "directions": []
    }

    done_with_map = False
    
    file = open("2024/15/input.txt", "r")
    
    for i, line in enumerate(file):
        line = line.replace('\n', '').replace('\r', '')
        if not done_with_map:
            if line == '':
                done_with_map = True
                continue

            for j, char in enumerate(line):
                if char == '.':
                    continue
                output['map'][char].append((j, i))
        else:
            for direction in line:
                output['directions'].append(direction)
            
            

    return output

if __name__ == '__main__':
    main()