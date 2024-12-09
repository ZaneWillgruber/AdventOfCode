import re

def main():
    part1()
    part2()

def part1():
    equations = parseFile()
    running_total = 0

    for equation in equations:
        if equation == "don't()" or equation == "do()":
            continue
        running_total += evalEquation(equation)

    print(running_total)

def part2():
    equations = parseFile()
    running_total = 0
    enabled = True

    for equation in equations:
        if equation == "don't()":
            enabled = False
            continue
        if equation == "do()":
            enabled = True
            continue
        
        if enabled:
            running_total += evalEquation(equation)

    print(running_total)

def parseFile():
    matches = []
    file = open("2024/3/input.txt", "r")
    
    for x in file:
        y = re.findall("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", x)
        matches += y

    return matches

def evalEquation(equation: str) -> int:
    nums = re.findall("\d{1,3}", equation)
    return int(nums[0]) * int(nums[1])

if __name__ == '__main__':
    main()