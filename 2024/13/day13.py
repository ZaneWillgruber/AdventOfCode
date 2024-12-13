def main():
    part1()
    part2()

def part1():
    return
    
def part2():
    return

def parseFile():
    output = []

    file = open("2024/13/testinput.txt", "r")
    
    for line in file:
        line = line.replace('\n', '').replace('\r', '')
        
        output.append(list(line))

    return output

if __name__ == '__main__':
    main()