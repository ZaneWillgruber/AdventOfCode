def main():
    #read the input file
    f = open("Day 1/input.txt", "r")
    lines = f.readlines()

    max = 0
    total = 0
    top3 = [0, 0, 0]

    for line in lines:
        if line != "\n":
            total += int(line)
        else:
            if total > min(top3):
                max = total
                top3.sort()
                top3[0] = max
            total = 0
            

    top3total = 0
    for i in top3:
        top3total += i

    print(max)
    print(top3total)

if __name__ == "__main__":
    main()