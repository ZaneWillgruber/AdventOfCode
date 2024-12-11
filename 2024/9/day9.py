from operator import add, mul

def main():
    part1()
    part2()

def part1():
    disk_map = parseFile()

    left_index = 0
    right_index = len(disk_map) - 1

    while left_index < right_index:
        while disk_map[left_index] != '.':
            left_index += 1

        while disk_map[right_index] == '.':
            right_index -= 1

        if left_index < right_index:
            swap(disk_map, left_index, right_index)

    running_total = check_sum(disk_map)

    print(running_total)

def part2():
    disk_map = parseFile()

    left_index = 0
    left_length = 1

    right_index = len(disk_map) - 1
    right_length = 1

    while left_index < right_index:
        while disk_map[right_index] == '.':
            right_index -= 1

        while disk_map[right_index] != '.' and disk_map[right_index - 1] == disk_map[right_index]:
            right_index -= 1
            right_length += 1

        while disk_map[left_index] != '.':
            left_index += 1
      


def swap(string, x, y):
    temp = string[x]
    string[x] = string[y]
    string[y] = temp

def check_sum(disk_map):
    running_total = 0

    for i in range(len(disk_map)):
        if disk_map[i] == '.':
            break

        running_total += i * int(disk_map[i])
    
    return running_total

def parseFile():
    output = []
    file_index = 0
    file = open("2024/9/testinput.txt", "r")
    
    for line in file:
        line = line.replace('\n', '').replace('\r', '')
        for i in range(len(line)):
            if i % 2 == 0:
                for j in range(int(line[i])):
                    output.append(str(file_index))
                file_index += 1
            else:
                for z in range(int(line[i])):
                    output.append('.')

    return output

if __name__ == '__main__':
    main()