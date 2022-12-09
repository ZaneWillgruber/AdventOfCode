def main():
    # Read input
    f = open("AdventOfCode2022/Day 3/input.txt", "r")
    lines = f.readlines()

    sum = 0;

    for line in lines:
        line = line.strip()
        line1 = line[0: int(len(line) / 2)]
        line2 = line[int(len(line) / 2): len(line)]

        for i in range(0, len(line1)):
            if line1[i] in line2:
                if line1[i].islower():
                    sum += ord(line1[i]) - 96
                    break
                else:
                    sum += ord(line1[i]) - 38
                    break

    print(sum)

if __name__ == '__main__':
    main()