from functools import cache

def main():
    part1()
    part2()

def part1():
    running_total = 0
    stones = parseFile()
    for stone in stones:
        running_total += blink(int(stone), 25)

    print('Part 1: ' + str(running_total))
    

def part2():
    running_total = 0
    stones = parseFile()
    for stone in stones:
        running_total += blink(int(stone), 75)

    print('Part 1: ' + str(running_total))

@cache
def blink(stone, count):
    while count > 0:
        if stone == 0:
            stone = 1
            count -= 1
        elif len(str(stone)) % 2 == 0:
            first_half = str(stone)[:len(str(stone)) // 2]
            second_half = str(stone)[len(str(stone)) // 2:]
            count -= 1
            total = 0
            total += blink(int(first_half), count)
            total += blink(int(second_half), count)
            return total
        else:
            stone = stone * 2024
            count -= 1

    return 1

    # while i < len(stones):
    #     if stones[i] == '0':
    #         stones[i] = '1'
    #     elif len(stones[i]) % 2 == 0:
    #         left_string = (stones[i][:int(len(stones[i]) / 2)]).lstrip('0')
    #         right_string = (stones[i][int(len(stones[i]) / 2):]).lstrip('0')
    #         stones.insert(i + 1, right_string if right_string != '' else '0')
    #         stones[i] = left_string if left_string != '' else '0'
    #         i += 1
    #     else:
    #         stones[i] = str(int(stones[i]) * 2024)

    #     i += 1

    # blink(stones, count - 1)

def parseFile():
    output = []

    file = open("2024/11/input.txt", "r")
    
    for line in file:
        line = line.replace('\n', '').replace('\r', '')
        
        output = line.split()

    return output

if __name__ == '__main__':
    main()