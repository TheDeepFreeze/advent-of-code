from collections import deque
from itertools import product
f = open("day12_input.txt")

text = f.readlines()

puzzle = []
visited = []
for line in text:
    puzzle.append(line.strip())
    visited.append(list("." for i in range(len(line.strip()))))

# [Marker, Area, Perimeter]
plotInfo = []

def isValid(x, y):
    if x < len(puzzle) and x >= 0 and y < len(puzzle[0]) and y >= 0:
        return True
    return False

# Find all the plants in the garden plot
def search(x, y):
    plant = puzzle[x][y]
    area = 0
    perimeter = 0
    q = deque()
    q.append([x, y])
    edges = []
    regions = []
    while q:
        cur = q.popleft()
        cx, cy = cur
        if visited[cx][cy] == "X":
            continue    
        visited[cx][cy] = "X"
        if cur not in regions:
            regions.append(cur)
        area += 1
        if isValid(cx + 1, cy) and puzzle[cx + 1][cy] == plant:
            if visited[cx + 1][cy] == ".":
                q.append([cx + 1, cy])
        else:
            edges.append([cx + 1, cy])
            perimeter += 1
        if isValid(cx - 1, cy) and puzzle[cx - 1][cy] == plant:
            if visited[cx - 1][cy] == ".":
                q.append([cx - 1, cy])
        else:
            edges.append([cx - 1, cy])
            perimeter += 1
        if isValid(cx, cy + 1) and puzzle[cx][cy + 1] == plant:
            if visited[cx][cy + 1] == ".":
                q.append([cx, cy + 1])
        else:
            edges.append([cx, cy + 1])
            perimeter += 1
        if isValid(cx, cy - 1) and puzzle[cx][cy - 1] == plant:
            if visited[cx][cy - 1] == ".":
                q.append([cx, cy - 1])
        else:
            edges.append([cx, cy - 1])
            perimeter += 1
    # Consolidate edge regions
    corners = 0
    for point in regions:
        row, col = point
        
        for row_off, col_off in product([1, -1], repeat=2):
            row_n = [row + row_off, col]
            col_n = [row, col + col_off]
            diag = [row + row_off, col + col_off]

            if row_n not in regions and col_n not in regions:
                corners += 1
            
            if (
                row_n in regions
                and col_n in regions
                and diag not in regions
            ):
                corners += 1


    return plant, area, perimeter, corners



for x in range(len(puzzle)):
    for y in range(len(puzzle[0])):
        if visited[x][y] == ".":
            plotInfo.append(search(x, y))
print(plotInfo)
totalprice = 0
discprice = 0
for plot in plotInfo:
    totalprice += plot[1] * plot[2]
    discprice += plot[1] * plot[3]
# 1396562
print(totalprice)

# Part 2
# 844132
print(discprice)



