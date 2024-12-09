def main():
    #part1()
    part2()

def part1():
    reports = parseFile()
    safecount = 0

    for report in reports:
        if isSafe(report):
            safecount += 1

    print(safecount)

def part2():
    reports = parseFile()
    safecount = 0

    for report in reports:
        if isSafe2(report):
            safecount += 1

    print(safecount)

def parseFile():
    reports = []
    file = open("2024/2/input.txt", "r")
    
    for x in file:
        x = x.replace('\n', '').replace('\r', '')
        numbers = x.split(" ")
        toAppend = []
        for n in numbers:
            toAppend.append(int(n))
        reports.append(toAppend)

    return reports

def isSafe(level):
    increasingArray = level.copy()
    increasingArray.sort()
    decreasingArray = increasingArray.copy()
    decreasingArray.reverse()

    if level != increasingArray and level != decreasingArray:
        return False

    for i in range(0, len(level) - 1):
        current = level[i]
        next = level[i+1]   

        if abs(current - next) > 3 or current == next:
            return False
        
    return True

def isSafe2(level):
    increasing = False

    for i in range(0, len(level) - 1):
        current = level[i]
        next = level[i+1]

        if i == 0:
            if current >= next:
                increasing = False
            else:
                increasing = True

        if abs(current - next) > 3 or current == next:
            return doubleCheck(level, i)
        
        if increasing:
            if current > next:
                return doubleCheck(level, i)
        else:
            if current < next:
                return doubleCheck(level, i)

            
        
    return True
                
def doubleCheck(level, i):
    toAppend = []
    otherAppend = []
    for j in range(0, len(level)):
        if i+1 != j:
            toAppend.append(level[j])

    for j in range(0, len(level)):
        if i != j:
            otherAppend.append(level[j])
    
    return isSafe(toAppend) or isSafe(otherAppend)


if __name__ == '__main__':
    main()