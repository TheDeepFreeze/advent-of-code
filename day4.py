f = open("day4_input.txt")

text = f.readlines()
puzzle = []
for line in text:
    temp = []
    for s in line:
        if s != "\n":
            temp.append(s)
    puzzle.append(temp)

total = 0
rows = len(puzzle)
cols = len(puzzle[0])
for r in range(rows):
    for c in range(cols):
        if puzzle[r][c] == "X":
            if r >= 3:
                # North
                if puzzle[r - 1][c] == "M" and puzzle[r - 2][c] == "A" and puzzle[r - 3][c] == "S":
                    total += 1
                # NW
                if c >= 3 and puzzle[r - 1][c - 1] == "M" and puzzle[r - 2][c - 2] == "A" and puzzle[r - 3][c - 3] == "S":
                    total += 1
                # NE
                if c < cols - 3 and puzzle[r - 1][c + 1] == "M" and puzzle[r - 2][c + 2] == "A" and puzzle[r - 3][c + 3] == "S":
                    total += 1
            if r < rows - 3:
                # South
                if puzzle[r + 1][c] == "M" and puzzle[r + 2][c] == "A" and puzzle[r + 3][c] == "S":
                    total += 1
                # SW
                if c >= 3 and puzzle[r + 1][c - 1] == "M" and puzzle[r + 2][c - 2] == "A" and puzzle[r + 3][c - 3] == "S":
                    total += 1
                # SE
                if c < cols - 3 and puzzle[r + 1][c + 1] == "M" and puzzle[r + 2][c + 2] == "A" and puzzle[r + 3][c + 3] == "S":
                    total += 1
            # West
            if c >= 3 and puzzle[r][c - 1] == "M" and puzzle[r][c - 2] == "A" and puzzle[r][c - 3] == "S":
                    total += 1
            # East
            if c < cols - 3 and puzzle[r][c + 1] == "M" and puzzle[r][c + 2] == "A" and puzzle[r][c + 3] == "S":
                    total += 1
# 2578
print(total)

# Part 2
cross = 0
for r in range(rows):
    for c in range(cols):
        if puzzle[r][c] == "A":
            if r > 0 and r < rows - 1 and c > 0 and c < cols - 1:
                comb = ["MMSS", "MSMS", "SMSM", "SSMM"]
                temp = ""
                temp += puzzle[r - 1][c - 1]
                temp += puzzle[r - 1][c + 1]
                temp += puzzle[r + 1][c - 1]
                temp += puzzle[r + 1][c + 1]
                if temp in comb:
                    cross += 1
print(cross)