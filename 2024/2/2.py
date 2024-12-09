def is_safe(s: str) -> bool:
    prev = int(s[0])
    increase = True
    decrease = True
    for curr in s[1:]:
        curr = int(curr)
        # inreasing
        if (prev == curr + 1) or (prev == curr + 2) or (prev == curr + 3):
            decrease = False
        # decreasing
        elif (prev == curr - 1) or (prev == curr - 2) or (prev == curr - 3):
            increase = False
        else: 
            return False
        prev = curr
        if (not decrease) and (not increase):
                return False
    return True

with open("2024/2/input.txt", "r") as data:
    count = 0
    while True:
        line = data.readline()
        if not line:
            break
        if is_safe(line.rstrip().split(' ')):
            count += 1

print('Answer to question 1: {}'.format(count))


with open("2/input.txt", "r") as data:
    count = 0
    while True:
        line = data.readline()
        if not line:
            break
        line_list = line.rstrip().split(' ')
        if is_safe(line_list):
            count += 1
        else:
            for i in range(len(line_list)):
                if is_safe((line_list[0:i] + line_list[i+1:])):
                    count +=1
                    break

print('Answer to question 2: {}'.format(count))