from operator import add, mul

def main():
    part1()
    part2()

def part1():
    running_total = 0

    input = parseFile()
    for x in input:
        running_total += solve(x, ops=[add, mul])

    print('Part 1: ' + str(running_total))

def part2():
    running_total = 0

    input = parseFile()
    for x in input:
        running_total += solve(x, ops=[add, mul, cat])

    print('Part 2: ' + str(running_total))

def cat(x: int, y: int):
    return int(str(x) + str(y))

def solve(nums, ops):
    if len(nums) == 2:
        return nums[0] == nums[1]
    
    total, a, b, *rest = nums
    for op in ops:
        if solve([total, op(a, b)] + rest, ops):
            return total
    return 0

def parseFile():
    return [list(map(int, line.replace(':','').split())) for line in open('2024/7/input.txt')]

if __name__ == '__main__':
    main()