def main():
    part1()
    part2()

def part1():
    grid = parseFile()
    running_total = 0
    directions = ["up", "down", "left", "right", "up-left", "up-right", "down-left", "down-right"]

    for x in grid["X"]:
        for direction in directions:
            next_coord = give_next_coord(x, direction)
            if next_coord in grid["M"]:
                next_coord = give_next_coord(next_coord, direction)
                if next_coord in grid["A"]:
                    next_coord = give_next_coord(next_coord, direction)
                    if next_coord in grid["S"]:
                        running_total += 1

    print("Part 1: " + str(running_total))

def part2():
    grid = parseFile()
    running_total = 0
    directions = ["up-left", "up-right", "down-left", "down-right"]

    for a in grid["A"]:
        m = []
        s = []
        for direction in directions:
            next_coord = give_next_coord(a, direction)
            if next_coord in grid["M"]:
                m.append(next_coord)
            elif next_coord in grid["S"]:
                s.append(next_coord)

        if len(m) != 2 or len(s) != 2:
            continue

        if s[0][0] == s[1][0] or s[0][1] == s[1][1]:
            running_total += 1

    print("Part 2: " + str(running_total))


def give_next_coord(coord, direction):
    
    if direction == "up":
        return [coord[0], coord[1] - 1]
    elif direction == "down":
        return [coord[0], coord[1] + 1]
    elif direction == "left":
        return [coord[0] - 1, coord[1]]
    elif direction == "right":
        return [coord[0] + 1, coord[1]]
    elif direction == "up-left":
        return [coord[0] - 1, coord[1] - 1]
    elif direction == "up-right":
        return [coord[0] + 1, coord[1] - 1]
    elif direction == "down-left":
        return [coord[0] - 1, coord[1] + 1]
    elif direction == "down-right":
        return [coord[0] + 1, coord[1] + 1]

def parseFile():
    locations = {}
    file = open("2024/4/input.txt", "r")
    current_point = [0, 0]
    
    for x in file:
        x = x.replace('\n', '').replace('\r', '')
        for y in x:
            if y in locations:
                copy = locations[y]
                copy.append(current_point)
                locations[y] = copy
            else:
                locations[y] = [current_point]

            current_point = [current_point[0], current_point[1] + 1]
        current_point = [current_point[0] + 1, 0]


    return locations

if __name__ == '__main__':
    main()