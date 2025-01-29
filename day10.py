from collections import deque
f = open("day10_input.txt")

puzzle = f.readlines()
for i in range(len(puzzle)):
    puzzle[i] = puzzle[i].strip()

# Find all trailheads
def findTrailheads(puzzle):
    trailheads = []
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == "0":
                trailheads.append([i, j])
    return trailheads

def isValid(puzzle, x, y):
    if x < len(puzzle) and x >= 0 and y < len(puzzle[0]) and y >= 0:
        return True
    return False

# Calculate each trailhead's score & rating
def calcTrailScore(puzzle, trailheads):
    scores = []
    ratings = []
    for trailhead in trailheads:
        q = deque()
        q.append([trailhead[0], trailhead[1], 0])
        peaks = []
        score = 0
        rating = 0
        while q:
            cur = q.popleft()
            x, y, val = cur
            if val == 9:
                rating += 1
                if [x, y] not in peaks:
                    score += 1
                    peaks.append([x, y])
                continue
            if isValid(puzzle, x + 1, y):
                if puzzle[x + 1][y] != "." and int(puzzle[x + 1][y]) == val + 1:
                    q.append([x + 1, y, val + 1])
            if isValid(puzzle, x - 1, y):
                if puzzle[x - 1][y] != "." and int(puzzle[x - 1][y]) == val + 1:
                    q.append([x - 1, y, val + 1])
            if isValid(puzzle, x, y + 1):
                if puzzle[x][y + 1] != "." and int(puzzle[x][y + 1]) == val + 1:
                    q.append([x, y + 1, val + 1])
            if isValid(puzzle, x, y - 1):
                if puzzle[x][y - 1] != "." and int(puzzle[x][y - 1]) == val + 1:
                    q.append([x, y - 1, val + 1])
        scores.append(score)
        ratings.append(rating)
    return scores, ratings

total = 0
trailheads = findTrailheads(puzzle)
scores, ratings = calcTrailScore(puzzle, trailheads)
for score in scores:
    total += score
# 638
print(total)

# Part 2
totalRating = 0
for rating in ratings:
    totalRating += rating
# 1289
print(totalRating)
    
                