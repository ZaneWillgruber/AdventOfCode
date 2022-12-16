def main():
    # Read input
    f = open("AdventOfCode2022/Day 11/input.txt", "r")
    lines = f.readlines()

    monkeys = []

    for line in lines:
        line = line.strip()
        if line.startswith("Monkey"):
            monkeys.append(Monkey())
        elif line.startswith("Starting items"):
            line = line[16:].split(", ")
            for item in line:
                monkeys[len(monkeys) - 1].items.append(int(item))
        elif line.startswith("Operation"):
            monkeys[len(monkeys) - 1].operation = line[17:]
        elif line.startswith("Test"):
            monkeys[len(monkeys) - 1].test = int(line[19:])
        elif line.startswith("If true"):
            line = line.split(" ")
            monkeys[len(monkeys) - 1].true = int(line[5])
        elif line.startswith("If false"):
            line = line.split(" ")
            monkeys[len(monkeys) - 1].false = int(line[5])

    worry = 1
    for monkey in monkeys:
        worry *= monkey.test

    for i in range(0, 10000):
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                monkey.count += 1
                currentWorry = worryOperation(monkey.items[0], monkey.operation) % worry
                monkey.items.remove(monkey.items[0])
                monkeys[monkey.true if (
                    currentWorry % monkey.test == 0) else monkey.false].items.append(currentWorry)

    max1 = 0
    max2 = 0
    for monkey in monkeys:
        if monkey.count > max1:
            max2 = max1
            max1 = monkey.count
        elif monkey.count > max2:
            max2 = monkey.count

    print(max1 * max2)


def worryOperation(old, factor):
    factor = factor.split(" ")
    if factor[2] == "old":
        factor[2] = old
    if factor[1] == "+":
        return old + int(factor[2])
    elif factor[1] == "*":
        return old * int(factor[2])


class Monkey:
    def __init__(self):
        self.items = []
        self.operation = ''
        self.test = 0
        self.true = 0
        self.false = 0
        self.count = 0


if __name__ == '__main__':
    main()
