register = 1
cycle = 0

def main():
    # Read input
    f = open("AdventOfCode2022/Day 10/input.txt", "r")
    lines = f.readlines()
    screen = []

    for i in range(6):
        screen.append([])
        for j in range(40):
            screen[i].append(".")
    
    global register, cycle

    for line in lines:
        line = line.strip()       
        
        if "noop" in line:
            screen = drawPixel(screen)
            cycle += 1
            continue
        else:
            line = line.split(" ")
            for i in range(2):
                screen = drawPixel(screen)
                cycle += 1
            register += int(line[1])

    printScreen(screen)

def printScreen(screen):
    for i in range(6):
        for j in range(40):
            print(screen[i][j], end="")
        print()

def drawPixel(screen):
    global register, cycle
    x = (cycle) // 40
    y = (cycle) % 40

    sprite = range(register - 1, register + 2)

    if y in sprite:
        screen[x][y] = "#"
    else:
        screen[x][y] = "."

    return screen

if __name__ == '__main__':
    main()