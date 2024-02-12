class Directory:
    
    def __init__(self, name):
        self.name = name
        self.files = []
        self.directories = []
    
    def __str__(self, level=0):
        indent = "  " * level
        result = f"{indent}/{self.name}  \t<DIR>\n"
        
        for subdir in self.directories:
            result += subdir.__str__(level + 1)

        for file in self.files:
            result += file.__str__(level + 1)


        return result
    
    def getSubDir(self, subName):
        for subDir in self.directories:
            if subDir.name == subName:
                return subDir
    
    def addFile(self, file):
        self.files.append(file)
        
    def addDirectory(self, dir):
        self.directories.append(dir)
    
    def totalSize(self):
        size = 0
        for file in self.files:
            size += file.size
        
        for subDir in self.directories:
            size += subDir.totalSize()
        
        return size
    
    def sizeBelow(self, maxSize = 100_000):
        size = self.totalSize()
        if size < maxSize:
            return size
        return 0
    
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)
    
    def __str__(self, level=0):
        indent = "  " * level
        return f"{indent}- {self.name}  \t({self.size})\n"

def main():
    with open("input_07.txt", 'r') as f:
        lines = f.readlines()
        home = Directory("/")
        stack = [home]
        
        dirs = [home]
        
        for line in lines:
            #print(f"> {line}", end = "")
            line = line.split()
            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "/":
                        stack = [home]
                        continue
                    elif line[2] == "..":
                        stack.pop()
                        continue
                    else:
                        #print("MOVE INTO DIR")
                        stack.append(stack[-1].getSubDir(line[2]))
                if line[1] == "ls":
                    #print("list stuff i guess")
                    pass
            elif line[0] == "dir":
                #print("FOUND DIR")
                #print(line[1])
                dir = Directory(line[1])
                stack[-1].addDirectory(dir)
                dirs.append(dir)
            else:
                #print(f"FOUND FILE: {line}")
                stack[-1].addFile(File(line[1], line[0]))
        
        print("\n- this is how the System looks -\n")
        print(home)
        print("Home total Size : ", home.totalSize())
        
        # solve A
        print(sum(map(Directory.sizeBelow, dirs)))
        
        # solve B
        
        diskSize   = 70_000_000
        updateSize = 30_000_000
        
        deleteAmount = updateSize - (diskSize - home.totalSize())

        print(deleteAmount)
        
        minDirSize = home.totalSize()
        
        for dir in dirs:
            size = dir.totalSize()
            if size < deleteAmount:
                continue
            
            minDirSize = min(minDirSize, size)
        
        print(minDirSize)
        

if __name__ == "__main__":
    main()