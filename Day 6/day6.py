def main():
    #read the input file
    f = open("Day 6/input.txt", "r")
    lines = f.readlines()

    line = lines[0]

    packet = line[0:3]
    chars = 0

    for char in range(3, len(line)):
        if line[char] in packet:
            packet = packet[1:] + line[char]
            packet = checkpacket(packet)
            continue
        else:
            packet = packet + line[char]
        
        if len(packet) == 4:
            chars = char
            break

    print(chars + 1)
    print(packet)

def checkpacket(packet):
    #check if packet has unique chars
    for char in range(0, len(packet[:len(packet) - 1])):
        if packet[char] in packet[char + 1:]:
            packet = packet[char + 1:]
            return checkpacket(packet)
    
    return packet

if __name__ == "__main__":
    main()