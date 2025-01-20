f = open("day1_input.txt")

col1, col2 = [], []
for line in f:
    col1.append(line.split()[0])
    col2.append(line.split()[1])

col1 = sorted(col1)
col2 = sorted(col2)

total = 0
for x, y in zip(col1, col2):
    total += abs(int(x) - int(y))

# 1879048
print(total)

# Part 2
freq, sim = {}, {}

for y in col2:
    freq[y] = freq.get(y, 0) + 1

totalSim = 0
for x in col1:
    sim[x] = freq.get(x, 0) * int(x)
    totalSim += sim[x]
# 21024792
print(totalSim)