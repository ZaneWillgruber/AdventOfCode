from operator import add, mul

def main():
    part1()
    part2()

def part1():
    output = parseFile()
    map = output['map']
    start_points = output['path_starts']

    find_path(map, start_points)

    running_total = 0

    for point in start_points:
        running_total += point['path_count']

    print('Part 1: ' + str(running_total))

def part2():
    output = parseFile()
    map = output['map']
    start_points = output['path_starts']

    find_path(map, start_points, True)

    running_total = 0

    for point in start_points:
        running_total += point['path_count']

    print('Part 2: ' + str(running_total))
      
def find_path(map, start_points, allow_multiple=False):
    x = len(map)
    y = len(map[0])

    for point in start_points:
        point['path_count'] = dfs(map, '0123456789', point['coords'][0], point['coords'][1], x, y, 0, point['top_visited'], allow_multiple)

def dfs(map, string, i, j, x, y, index, visited, allow_multiple):
    if i < 0 or i >= x or j < 0 or j >= y:
        return 0
    if string[index] != map[i][j]:
        return 0
    if index == len(string) - 1:
        if allow_multiple:
            return 1
        if not [i, j] in visited:
            visited.append([i, j])
            return 1
        return 0
    
    temp = map[i][j]
    map[i][j] = '*'
    a = dfs(map, string, i, j + 1, x, y, index + 1, visited, allow_multiple)
    b = dfs(map, string, i, j - 1, x, y, index + 1, visited, allow_multiple)
    c = dfs(map, string, i + 1, j, x, y, index + 1, visited, allow_multiple)
    d = dfs(map, string, i - 1, j, x, y, index + 1, visited, allow_multiple)
    map[i][j] = temp

    return a + b + c + d

def parseFile():
    output = {
        'map': [],
        'path_starts': []
    }

    current_coords = [0, 0]

    file = open("2024/10/input.txt", "r")
    
    for line in file:
        line = line.replace('\n', '').replace('\r', '')
        toAppend = []
        for char in line:
            toAppend.append(char)

            if char == '0':
                output['path_starts'].append({'coords': current_coords, 'path_count': 0, 'top_visited': []})

            current_coords = [current_coords[0], current_coords[1] + 1]

        current_coords = [current_coords[0] + 1, 0]
        output['map'].append(toAppend)

    return output

if __name__ == '__main__':
    main()