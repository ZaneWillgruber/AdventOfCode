def main():
    #read the input file
    f = open("Day 4/input.txt", "r")
    lines = f.readlines()

    overlapCount = 0

    for line in lines:
        line = line.strip()
        line = line.split(",")

        elf1 = line[0].split("-")
        elf2 = line[1].split("-")

        #convert to ints
        elf1 = [int(x) for x in elf1]
        elf2 = [int(x) for x in elf2]

        if elf1[0] >= elf2[0] and elf1[0] <= elf2[1]:
            overlapCount += 1
        elif elf1[1] >= elf2[0] and elf1[1] <= elf2[0]:
            overlapCount += 1
        elif elf2[0] >= elf1[0] and elf2[0] <= elf1[1]:
            overlapCount += 1
        elif elf2[1] >= elf1[0] and elf2[1] <= elf1[1]:
            overlapCount += 1

    print(overlapCount)

if __name__ == "__main__":
    main()