import os

def main():
    #read the input file
    f = open("Day 1/input.txt", "r")
    lines = f.readlines()

    max = 0
    total = 0

    for line in lines:
        if line != "\n":
            total += int(line)
        else:
            if total > max:
                max = total
            total = 0

        
    print(max)

if __name__ == "__main__":
    main()