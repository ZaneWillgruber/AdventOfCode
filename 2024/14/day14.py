import re

def main():
    part1()
    part2()

def part1():
    input = parseFile()

    width = 101
    height = 103

    final_locations = {
        'ne': [],
        'nw': [],
        'se': [],
        'sw': []
    }

    for robot in input:
        position_x, position_y, velocity_x, velocity_y = map(int, re.findall('-?\d+', robot))
        robot_location = move_robot(position_x, position_y, velocity_x, velocity_y, width, height, 100)
        if robot_location[0] < width // 2 and robot_location[1] < height // 2:
            final_locations['nw'].append(robot_location)
        elif robot_location[0] > width // 2 and robot_location[1] < height // 2:
            final_locations['ne'].append(robot_location)
        elif robot_location[0] < width // 2 and robot_location[1] > height // 2:
            final_locations['sw'].append(robot_location)
        elif robot_location[0] > width // 2 and robot_location[1] > height // 2:
            final_locations['se'].append(robot_location)

    print(f'Part 1: {len(final_locations["ne"]) * len(final_locations["nw"]) * len(final_locations["se"]) * len(final_locations["sw"])}')
    
def part2():
    output = parseFile()

    width = 101
    height = 103
    steps = 0

    while True:
        opposite_matches = 0
        locations = set()
        image = [['░' for i in range(width)] for j in range(height)]

        for robot in output:
            position_x, position_y, velocity_x, velocity_y = map(int, re.findall('-?\d+', robot))
            robot_location = move_robot(position_x, position_y, velocity_x, velocity_y, width, height, steps)
            locations.add(robot_location)
            image[robot_location[1]][robot_location[0]] = '█'


        for loc in locations:
            if loc[0] < width // 2:
                if (width // 2 + (width // 2 - loc[0]), loc[1]) in locations:
                    opposite_matches += 1

        if opposite_matches < 70:
            steps += 1
            continue
        

        for i in image:
            print("".join(i))

        print(f'Part 2: {steps}')

        break

def move_robot(position_x, position_y, velocity_x, velocity_y, width, height, steps):
    return ((position_x + velocity_x * steps) % width, (position_y + velocity_y * steps) % height)

def parseFile():
    output = []
    
    with open("2024/14/input.txt", "r") as file:
        chunks = file.read().split('\n')

    return chunks

if __name__ == '__main__':
    main()