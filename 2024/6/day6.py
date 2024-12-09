import time

def main():
    part1()
    part2()

def part1():
    output = parseFile()
    obstacles = output['obstacles']
    guard_location = output['guard_location']
    upper_bound = output['upper_bound']
    current_direction = 'up'
    has_been_to = steps_on_path(guard_location, upper_bound, obstacles, current_direction) 

    print("Part 1: " + str(has_been_to['steps']))

def can_move(obstacles, guard_location, direction):
    if get_next_location(guard_location, direction) in obstacles:
        return False
    
    return True

def get_next_location(guard_location, direction):
    if direction == 'up':
        return [guard_location[0], guard_location[1] - 1]
    elif direction == 'down':
        return [guard_location[0], guard_location[1] + 1]
    elif direction == 'left':
        return [guard_location[0] - 1, guard_location[1]]
    elif direction == 'right':
        return [guard_location[0] + 1, guard_location[1]]
    
def get_next_direction(direction):
    if direction == 'up':
        return 'right'
    elif direction == 'right':
        return 'down'
    elif direction == 'down':
        return 'left'
    elif direction == 'left':
        return 'up'

def steps_on_path(guard_location, upper_bound, obstacles, current_direction):
    start_time = time.time()
    has_been_to = [guard_location]

    while guard_location[0] > -1 and guard_location[0] < upper_bound[0] and guard_location[1] > -1 and guard_location[1] < upper_bound[1]:
        if time.time() - start_time > 1:
            return {'steps': 0, "locations": has_been_to}

        if not guard_location in has_been_to:
            has_been_to.append(guard_location)

        while not can_move(obstacles, guard_location, current_direction):
            current_direction = get_next_direction(current_direction)

        guard_location = get_next_location(guard_location, current_direction) 

    return {'steps': len(has_been_to), "locations": has_been_to}

def part2():
    output = parseFile()
    obstacles = output['obstacles']
    guard_location = output['guard_location']
    upper_bound = output['upper_bound']
    current_direction = 'up'

    available = steps_on_path(guard_location, upper_bound, obstacles, current_direction)


    running_total = 0

    try_counter = 1
    for possible_point in available['locations']:
        print('Trying ' + str(try_counter) + " of " + str(len(available['locations'])))
        try_counter += 1
        test_obstacles = obstacles.copy()
        test_obstacles.append(possible_point)
        test_steps = steps_on_path(guard_location, upper_bound, test_obstacles, current_direction)
        if test_steps['steps'] < 0:
            running_total += 1

    print("Part 2: " + str(running_total))


def parseFile():
    output = {
        'obstacles': [],
        'available': [],
        'guard_location': [0,0],
        'upper_bound': [0,0]
    }
    
    file = open("2024/6/input.txt", "r")
    current_point = [0, 0]
    
    for line in file:
        line = line.replace('\n', '').replace('\r', '')
        for char in line:
            if char == '#':
                output['obstacles'].append(current_point)
            elif char == '^':
                output['guard_location'] = current_point
            else:
                output['available'].append(current_point)
            
            output['upper_bound'] = [current_point[0] + 1, current_point[1] + 1]
            current_point = [current_point[0] + 1, current_point[1]]
        
        current_point = [0, current_point[1] + 1]


    return output
        


    return locations

if __name__ == '__main__':
    main()