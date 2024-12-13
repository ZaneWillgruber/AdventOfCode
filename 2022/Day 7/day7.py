currentDirectory = None

def main():
    #read the input file
    f = open("Day 7/input.txt", "r")
    lines = f.readlines()
    global currentDirectory
    currentDirectory = Directory("/", None)
    root = currentDirectory

    for line in lines[1:]:
        if line[0] == "$":
            processCommand(line, currentDirectory)
        else:
            if line[0] == "d":
                line = line.strip()
                currentDirectory.subdirectories.append(Directory(line[4:], currentDirectory))
            else:
                line = line.strip()
                line = line.split(" ")
                currentDirectory.files.append(File(line[1], line[0]))

    totalSize = findSmallDirectorys(root)

    print(totalSize)
        
def processCommand(line, currentDirectory):
    line = line.strip()
    line = line.split(" ")
    command = line[1]

    if command == "cd":
        cd(line[2])
    elif command == "ls":
        ls(currentDirectory)

def cd(path):
    global currentDirectory
    if path == "..":
        currentDirectory = currentDirectory.parent
    else:
        for directory in currentDirectory.subdirectories:
            if directory.name == path:
                currentDirectory = directory
                return

def ls(currentDirectory):
    return

def findSmallDirectorys(directory):
    totalsize = 0
    size = directory.getFilesSize()

    if size <= 100000:
        totalsize += size

    for subdirectory in directory.subdirectories:
        totalsize += findSmallDirectorys(subdirectory)

    return totalsize

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subdirectories = []
        self.files = []
        self.size = 0

    def getFilesSize(self):
        for file in self.files:
            self.size += int(file.size)

        for subdirectory in self.subdirectories:
            self.size += subdirectory.getFilesSize()
            
        return self.size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size



if __name__ == "__main__":
    main()