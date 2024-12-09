leftList = []
rightList = []
frequencyDict = {}

def main():
    #part1()
    part2()

def part2():
    parseFile2()
    simScore = 0
    
    for n in leftList:
        if n in frequencyDict:
            simScore += int(n) * frequencyDict[n]

    print(simScore)

def part1():
    parseFile()
    leftList.sort()
    rightList.sort()

    totalDistance = 0

    for i in range(0, len(leftList)):
        distance = abs(int(leftList[i]) - int(rightList[i]))
        totalDistance += distance

    print(totalDistance)

def parseFile():
    file = open("2024/1/input.txt", "r")
    
    for x in file:
        x = x.replace('\n', ' ').replace('\r', '')
        numbers = x.split("   ")
        
        leftList.append(int(numbers[0]))
        rightList.append(int(numbers[1]))

def parseFile2():
    file = open("1/input.txt", "r")
    
    for x in file:
        x = x.replace('\n', '').replace('\r', '')
        numbers = x.split("   ")
        
        leftList.append(numbers[0])
        
        if numbers[1] in frequencyDict:
            frequencyDict[numbers[1]] = frequencyDict[numbers[1]] + 1
        else:
            frequencyDict[numbers[1]] = 1

if __name__ == "__main__":
    main()