from collections import defaultdict
f = open("day8_input.txt")

# Find all antennas
antennas = defaultdict(list)
text = f.readlines()
for r in range(len(text)):
    text[r] = text[r].strip()
    for c in range(len(text[0])):
        if text[r][c] != ".":
            antennas[text[r][c]].append([r, c])

def valid(x, y):
    if x >= 0 and x < len(text) and y >= 0 and y < len(text[0]):
        return True
    return False

antis = []

def antinode(antenna, positions):
    for a1 in range(len(positions)):
        for a2 in positions[a1 + 1:]:
            x1, y1 = positions[a1]
            x2, y2 = a2
            xdiff = x2 - x1
            ydiff = y2 - y1
            anti1x = x1 - xdiff
            anti1y = y1 - ydiff
            anti2x = x2 + xdiff
            anti2y = y2 + ydiff
            if valid(anti1x, anti1y) and [anti1x, anti1y] not in antis:
                antis.append([anti1x, anti1y])
            if valid(anti2x, anti2y) and [anti2x, anti2y] not in antis:
                antis.append([anti2x, anti2y])

antis2 = []
# Part 2
def antinode2(antenna, positions):
    for a1 in range(len(positions)):
        for a2 in positions[a1 + 1:]:
            x1, y1 = positions[a1]
            x2, y2 = a2
            xdiff = x2 - x1
            ydiff = y2 - y1
            anti1x = x1 - xdiff
            anti1y = y1 - ydiff
            while valid(anti1x, anti1y):
                if [anti1x, anti1y] not in antis2:
                    antis2.append([anti1x, anti1y])
                anti1x -= xdiff
                anti1y -= ydiff
            anti2x = x2 + xdiff
            anti2y = y2 + ydiff
            while valid(anti2x, anti2y):
                if [anti2x, anti2y] not in antis2:
                    antis2.append([anti2x, anti2y])
                anti2x += xdiff
                anti2y += ydiff
            if [x1, y1] not in antis2:
                antis2.append([x1, y1])
            if [x2, y2] not in antis2:
                antis2.append([x2, y2])  
            

for antenna, positions in antennas.items():
    antinode(antenna, positions)
    antinode2(antenna, positions)
# 220
print(len(antis))
# 813
print(len(antis2))
