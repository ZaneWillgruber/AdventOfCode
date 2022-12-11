def main():
    #read the input file
    f = open("Day 5/input.txt", "r")
    lines = f.readlines()

    stacks = [[], [], [], [], [], [], [], [], []]
    stacksCreated = False

    for line in lines:
        if line == " 1   2   3   4   5   6   7   8   9 \n":
            stacksCreated = True
            for stack in stacks:
                stack.reverse()
            continue

        if(stacksCreated == False):
            for i in range(1, len(line), 4):
                if line[i] != " ":
                    stacks[(int((i + 3) / 4)) - 1].append(line[i])
        else:
            if line == "\n":
                continue
            line = line.strip()
            line = line.split(" ")
            count = line[1]
            fromStack = line[3]
            toStack = line[5]
            move(count, fromStack, toStack, stacks)

    for stack in stacks:
        print(stack.pop())

def move(count, fromStack, toStack, stacks):
    tempStack = []
    for i in range(int(count)):
        tempStack.append(stacks[int(fromStack) - 1].pop())
    for i in range(int(len(tempStack))):
        stacks[int(toStack) - 1].append(tempStack.pop())

if __name__ == "__main__":
    main()