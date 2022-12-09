def main():
    # Read input
    f = open("AdventOfCode2022/Day 3/input.txt", "r")
    lines = f.readlines()

    sum = 0;

    for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
        l1 = l1.strip()
        l2 = l2.strip()
        l3 = l3.strip()

        for i in range(0, len(l1)):
            if l1[i] in l2 and l1[i] in l3:
                if l1[i].islower():
                    sum += ord(l1[i]) - 96
                    break
                else:
                    sum += ord(l1[i]) - 38
                    break

    print(sum)

if __name__ == '__main__':
    main()