symbols = {"A" : 0, "B" : 1, "C" : 2}

def main():
    #read the input file
    f = open("Day 2/input.txt", "r")
    lines = f.readlines()

    total = 0

    for line in lines:
        line = line.strip()
        played = line.split(" ")
        res = playgame(symbols[played[0]], played[1])
        total += res + 1

    print(total)

def playgame(a, z):
    if z == "X":
        return 0 + ((a - 1) % 3)
    elif z == "Y":
        return 3 + a
    else:
        return 6 + ((a + 1) % 3)

if __name__ == "__main__":
    main()