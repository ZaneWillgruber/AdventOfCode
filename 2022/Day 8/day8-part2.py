def main():
    # Read input
    f = open("AdventOfCode2022/Day 8/input.txt", "r")
    lines = f.readlines()

    maxScore = 0

    #Strip all lines
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    for i in range(1, len(lines) - 1):
        line = lines[i]
        for n in range(1, len(line) - 1):
            score = calcScore(n, i, lines)
            if score > maxScore:
                maxScore = score

    print(maxScore)

def calcScore(x, y, lines):
    score = [0, 0, 0, 0]
    for i in range(y - 1, -1, -1):
        if(int(lines[y][x]) > int(lines[i][x])):
            score[0] += 1
        else:
            score[0] += 1
            break

    for i in range(y + 1, len(lines)):
        if(int(lines[y][x]) > int(lines[i][x])):
            score[1] += 1
        else:
            score[1] += 1
            break

    for i in range(x - 1, -1, -1):
        if(int(lines[y][x]) > int(lines[y][i])):
            score[2] += 1
        else:
            score[2] += 1
            break

    for i in range(x + 1, len(lines[y])):
        if(int(lines[y][x]) > int(lines[y][i])):
            score[3] += 1
        else:
            score[3] += 1
            break
    calc = score[0] * score[1] * score[2] * score[3]

    return calc


if __name__ == '__main__':
    main()