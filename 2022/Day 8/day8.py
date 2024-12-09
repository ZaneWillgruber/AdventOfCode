def main():
    # Read input
    f = open("AdventOfCode2022/Day 8/input.txt", "r")
    lines = f.readlines()

    visibleCount = 0;

    #Strip all lines
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    for i in range(1, len(lines) - 1):
        line = lines[i]
        for n in range(1, len(line) - 1):
            if checkRow(n, i, lines, "up") or checkRow(n, i, lines, "down") or checkRow(n, i, lines, "left") or checkRow(n, i, lines, "right"):
                visibleCount += 1

    visibleCount += (len(lines[0]) * 2) + (len(lines) * 2) - 4

    print(visibleCount)

def checkRow(x, y, lines, direction):
    if(direction == "up"):
        for i in range(y - 1, -1, -1):
            if(int(lines[y][x]) <= int(lines[i][x])):
                return False
    elif(direction == "down"):
        for i in range(y + 1, len(lines)):
            if(int(lines[y][x]) <= int(lines[i][x])):
                return False
    elif(direction == "left"):
        for i in range(x - 1, -1, -1):
            if(int(lines[y][x]) <= int(lines[y][i])):
                return False
    elif(direction == "right"):
        for i in range(x + 1, len(lines[y])):
            if(int(lines[y][x]) <= int(lines[y][i])):
                return False
    return True


if __name__ == '__main__':
    main()