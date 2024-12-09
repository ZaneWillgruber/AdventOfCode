def main():
    # Read input
    f = open("AdventOfCode2022/Day 9/input.txt", "r")
    lines = f.readlines()

    visited = []
    tail = {'x': 0, 'y': 0}
    head = {'x': 0, 'y': 0}

    for line in lines:
        line = line.strip()
        line = line.split(" ")

        for i in range(int(line[1])):
            head = moveHead(head, line[0])
            tail = moveTail(tail, head)
            if (tail['x'], tail['y']) not in visited:
                visited.append((tail['x'], tail['y']))

    print(len(visited))

def moveHead(head, direction):
    if direction == "U":
        head['y'] += 1
    elif direction == "D":
        head['y'] -= 1
    elif direction == "L":
        head['x'] -= 1
    elif direction == "R":
        head['x'] += 1
    return head

def moveTail(tail, head):
    if tail['x'] == head['x'] and tail['y'] == head['y']:
        return tail
    else:
        if abs(tail['x'] - head['x']) <= 1 and abs(tail['y'] - head['y']) <= 1:
            return tail

        if tail['x'] < head['x']:
            tail['x'] += 1
        elif tail['x'] > head['x']:
            tail['x'] -= 1
        if tail['y'] < head['y']:
            tail['y'] += 1
        elif tail['y'] > head['y']:
            tail['y'] -= 1
        return tail

if __name__ == '__main__':
    main()