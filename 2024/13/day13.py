import re

def main():
    part1()
    part2()

def part1():
    input = parseFile()

    total = 0
    tolerance = .0001

    for machine in input:
        button_a_x, button_a_y, button_b_x, button_b_y, target_x, target_y = map(int, re.findall("\d+", machine))
        A = (button_b_x * target_y - button_b_y * target_x) / (button_b_x * button_a_y - button_b_y * button_a_x)
        B = (target_x - button_a_x * A) / button_b_x

        if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
            total += 3 * A + B

    total = int(total)

    print(f'Part 1: {total}')
    
def part2():
    input = parseFile()

    total = 0
    tolerance = .0001

    for machine in input:
        button_a_x, button_a_y, button_b_x, button_b_y, target_x, target_y = map(int, re.findall("\d+", machine))
        target_x += 10000000000000
        target_y += 10000000000000
        A = (button_b_x * target_y - button_b_y * target_x) / (button_b_x * button_a_y - button_b_y * button_a_x)
        B = (target_x - button_a_x * A) / button_b_x

        if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
            total += 3 * A + B

    total = int(total)

    print(f'Part 2: {total}')


def parseFile():
    output = []
    
    with open("2024/13/input.txt", "r") as file:
        chunks = file.read().split('\n\n')

    return chunks

if __name__ == '__main__':
    main()