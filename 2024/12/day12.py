def main():
    part1()
    part2()

def part1():
    output = parseFile()
    length_x = len(output)
    length_y = len(output[0])

    regions = []

    running_total = 0

    for x in range(length_x):
        for y in range(length_y):
            if output[x][y] != '*':
                match = output[x][y]
                test = find_connected(output, match, x, y, length_x, length_y)
                toAppend = {'flower': match, 'locations': test, 'count': len(test)}
                toAppend['perimeter'] = calculate_perimeter(toAppend['locations'])
                regions.append(toAppend)
    
    for i in range(len(regions)):
        running_total += regions[i]['count'] * regions[i]['perimeter']

    print(f'Part 1: {running_total}')
    
def find_connected(map, match, x, y, length_x, length_y):
    connected = []
    if x < 0 or x >= length_x or y < 0 or y >= length_y:
        return
    if match == map[x][y]:
        connected.append((x, y))
        map[x][y] = '*'
        a = find_connected(map, match, x, y + 1, length_x, length_y)
        b = find_connected(map, match, x, y - 1, length_x, length_y)
        c = find_connected(map, match, x + 1, y, length_x, length_y)
        d = find_connected(map, match, x - 1, y, length_x, length_y)

        if not a == None:
            connected = connected + a
        if not b == None:
            connected = connected + b
        if not c == None:
            connected = connected + c
        if not d == None:
            connected = connected + d

    return sorted(connected, key = lambda x: (x[0], x[1]))
        
def calculate_perimeter(points):
    # Convert points to a set for fast lookup
    point_set = set(points)
    perimeter = 0

    # Directions for neighboring points (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Check each point for exposed edges
    for x, y in points:
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor not in point_set:  # If no neighbor, it's a boundary edge
                perimeter += 1

    return perimeter

def get_sides(region):
    sides = 0

    edge_coord_corners = set()
    for x, y in region:
        for dx, dy in [(.5, .5), (.5, -.5), (-.5, .5), (-.5, -.5)]:
            edge_coord_corners.add((x + dx, y + dy))
    
    for x, y in edge_coord_corners:
        pattern = ""
        for dx, dy in [(.5, .5), (.5, -.5), (-.5, .5), (-.5, -.5)]: 
            pattern += "X" if (x+dx, y+dy) in region else "O"
        if pattern in ("OXXO", "XOOX"):
            # When an edge coord is two the region meets itself all catty-corner
            sides += 2
        elif pattern.count("X") == 3 or pattern.count("O") == 3:
            # For when an edge coord is an interior or exterior corner.
            sides += 1

    return sides

def part2():
    output = parseFile()
    length_x = len(output)
    length_y = len(output[0])

    regions = []

    running_total = 0

    for x in range(length_x):
        for y in range(length_y):
            if output[x][y] != '*':
                match = output[x][y]
                test = find_connected(output, match, x, y, length_x, length_y)
                toAppend = {'flower': match, 'locations': test, 'count': len(test)}
                toAppend['sides'] = get_sides(toAppend['locations'])
                regions.append(toAppend)
    
    for i in range(len(regions)):
        running_total += regions[i]['count'] * regions[i]['sides']

    print(f'Part 2: {running_total}')

def parseFile():
    output = []

    file = open("2024/12/input.txt", "r")
    
    for line in file:
        line = line.replace('\n', '').replace('\r', '')
        
        output.append(list(line))

    return output

if __name__ == '__main__':
    main()