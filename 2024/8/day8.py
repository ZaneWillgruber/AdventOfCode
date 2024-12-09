from operator import add, mul

def main():
    part1()
    part2()

def part1():
    output = parseFile()
    antennas = output['antennas']
    upper_bound = output['upper_bound']

    antinode_locations = []

    for key, value in antennas.items():
        for location in value:
            for test_against in value:
                if location == test_against:
                    continue

                next_location = find_next_possible_location(location, test_against)
                if in_bounds(upper_bound, next_location):
                    if not next_location in antinode_locations:
                        antinode_locations.append(next_location)

    print('Part 1: ' + str(len(antinode_locations)))

def part2():
    output = parseFile()
    antennas = output['antennas']
    upper_bound = output['upper_bound']

    antinode_locations = []

    for key, value in antennas.items():
        for location in value:
            for test_against in value:
                if location == test_against:
                    continue

                if not location in antinode_locations:
                        antinode_locations.append(location)
                
                _location = location
                next_location = find_next_possible_location(location, test_against)
                while in_bounds(upper_bound, next_location):
                    if not next_location in antinode_locations:
                        antinode_locations.append(next_location)

                    test_against = _location
                    _location = next_location
                    
                    next_location = find_next_possible_location(_location, test_against)

    print('Part 2: ' + str(len(antinode_locations)))

def find_next_possible_location(location, test_against):
    difference = [location[0] - test_against[0], location[1] - test_against[1]]
    return [location[0] + difference[0], location[1] + difference[1]]

def in_bounds(upper_bound, location):
    return location[0] > -1 and location[0] < upper_bound[0] and location[1] > -1 and location[1] < upper_bound[1]

def parseFile():
    output = {
        'antennas': {},
        'upper_bound': [0,0]
    }
    
    file = open("2024/8/input.txt", "r")
    current_point = [0, 0]
    
    for line in file:
        line = line.replace('\n', '').replace('\r', '')
        for char in line:
            if char != '.':
                if char in output['antennas']:
                    output['antennas'][char].append(current_point)
                else:
                    output['antennas'][char] = [current_point]
            
            output['upper_bound'] = [current_point[0] + 1, current_point[1] + 1]
            current_point = [current_point[0] + 1, current_point[1]]
        
        current_point = [0, current_point[1] + 1]


    return output

if __name__ == '__main__':
    main()