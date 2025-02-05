from collections import deque 
from collections import defaultdict
f = open("day9_input.txt")

# Create Initial file system

files = deque()
text = f.read().strip()
fid = 0
fspace = False
for num in text:
    for i in range(int(num)):
        if fspace:
            files.append(".")
        else:
            files.append(fid)
    if not fspace:
        fid += 1
        fspace = True
    else:
        fspace = False

# Adjust file system
for i in range(len(files)):
    if i < len(files) - 1 and files[i] == ".":
        block = "."
        while block == "." and len(files) - 1 > i:
            block = files.pop()
        files[i] = block

def calcsum(files):
    # calculate checksum
    checksum = 0
    for i in range(len(files)):
        if files[i] != ".":
            checksum += (i * files[i])
    return checksum
# 6386640365805
print(calcsum(files))

# Part 2

# Create file again and keep track of free space blocks
def createFile(text):
    files = deque()
    fid = 0
    maxfree = 0 
    # Key: # Free space blocks
    # Value: Index of free space
    # [# Free space blocks, Index of free space]
    free = []
    # Key: File ID
    # Value: File Length, Index of file
    file = defaultdict(list)
    fspace = False
    for num in text:
        if fspace:
            free.append([int(num), len(files)])
            maxfree = max(maxfree, int(num))
        else:
            file[fid] = [int(num), len(files)]
        for i in range(int(num)):
            if fspace:
                files.append(".")
            else:
                files.append(fid)
        if not fspace:
            fid += 1
            fspace = True
        else:
            
            fspace = False
    return files, free, fid, file, maxfree
files2, free, fid, file, maxfree = createFile(text)

def updatefree(files):
    free = []
    freefound = False
    start = 0
    for i in range(len(files)):
        cur = files[i]

        if not freefound and cur == ".":
            start = i
            freefound = True
        elif freefound:
            if cur != ".":
                free.append([i - start, start])
                freefound = False
    return free


# Fill free space
for fileID in range(fid - 1, -1, -1):
    flength, fidx = file[fileID]
    freelen = flength
    foundlen = 0

    for j in range(len(free)):

        if free[j][0] >= flength and free[j][1] < fidx:
            freeblock = free[j][1]
            foundlen = j
            # Remove original file & update free block
            for i in range(flength):
                files2[fidx + i] = "."
                files2[freeblock + i] = fileID
            break
    free = updatefree(files2)
    
    
    
        
# 6423258376982
print(calcsum(files2))
        

