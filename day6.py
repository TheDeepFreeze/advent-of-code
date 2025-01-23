f = open("day6_input.txt")
#f = open("temp")

text = f.readlines()

puzzle = []
for line in text:
    temp = []
    for c in line.strip():
        temp.append(c)
    puzzle.append(temp)

sr = 0
sc = 0

for row in range(len(puzzle)):
    for col in range(len(puzzle[0])):
        if puzzle[row][col] == "^":
            sr = row
            sc = col
            puzzle[row][col] = "."

pathlen = 0
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def findloop(sr, sc, cdir, path):
    cr, cc = sr, sc
    move = directions[cdir]
    tr = sr + move[0]
    tc = sc + move[1]
    if tr >= len(puzzle) or tr < 0 or tc >= len(puzzle[0]) or tc < 0:
        return False
    if puzzle[tr][tc] == "#" or [tr, tc, 0] in path or [tr, tc, 1] in path or [tr, tc, 2] in path or [tr, tc, 3] in path:
        return False
    old = puzzle[tr][tc]
    puzzle[tr][tc] = "#"
    temppath = []
    temppath.append([cr, cc, cdir])
    
    # Rotate once
    newdir = (cdir + 1) % 4
    
    while True:
        move = directions[newdir]
        nr = cr + move[0]
        nc = cc + move[1]
        if [cr, cc, newdir] not in temppath:
            temppath.append([cr, cc, newdir])
        if nr >= len(puzzle) or nr < 0 or nc >= len(puzzle[0]) or nc < 0:
            puzzle[tr][tc] = old
            return False
        if puzzle[nr][nc] == "#":
            newdir = (newdir + 1) % 4
        else:
            cr += move[0]
            cc += move[1]
        if [cr, cc, newdir] in path or [cr, cc, newdir] in temppath:
            puzzle[tr][tc] = old
            return True
        



curdir = 0
obs = 0
path = []
while True:
    if [sr, sc, curdir] not in path:
        
        if findloop(sr, sc, curdir, path):
            print(sr, sc, curdir)
            obs += 1
    if puzzle[sr][sc] == ".":
        puzzle[sr][sc] = "X"
        pathlen += 1
        path.append([sr, sc, curdir])
    
    move = directions[curdir]
    nr = sr + move[0]
    nc = sc + move[1]
    
    if nr >= len(puzzle) or nr < 0 or nc >= len(puzzle[0]) or nc < 0:
        break
    if puzzle[nr][nc] == "#":
        curdir = (curdir + 1) % 4
    else:
        sr += move[0]
        sc += move[1]
# 4665
print(pathlen)
# 1688
print(obs)