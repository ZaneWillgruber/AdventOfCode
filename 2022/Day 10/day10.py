register = 1
cycle = 0

def main():
    # Read input
    f = open("AdventOfCode2022/Day 10/input.txt", "r")
    lines = f.readlines()
    
    global register, cycle

    total = 0

    for line in lines:
        line = line.strip()       
        
        if "noop" in line:
            cycle += 1
            total += checkStrength()
            continue
        else:
            line = line.split(" ")
            for i in range(2):
                cycle += 1
                total += checkStrength()  
            register += int(line[1])

    print(total)

def checkStrength():
    global register, cycle
    if not (cycle-20)%40:
        return register * cycle
    return 0

if __name__ == '__main__':
    main()