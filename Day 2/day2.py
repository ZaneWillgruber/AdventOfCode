def main():
    #read the input file
    f = open("Day 2/input.txt", "r")
    lines = f.readlines()

    symbols = {"A" : 0, "B" : 1, "C" : 2, "X" : 0, "Y" : 1, "Z" : 2}

    total = 0

    for line in lines:
        line = line.strip()
        played = line.split(" ")
        res = playgame(symbols[played[0]], symbols[played[1]])
        total += res + (symbols[played[1]] + 1)

    print(total)

def playgame(a, z):
    if a == z:
        return 3
    elif z == (a + 1) % 3:
        return 6
    else:
        return 0

if __name__ == "__main__":
    main()