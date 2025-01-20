f = open("day2_input.txt")

numSafe = 0
unsafe = []
for line in f:
    report = line.split()
    start = int(report[0])
    pole = True
    safe = True
    if int(report[0]) - int(report[1]) < 0:
        pole = False
    for i in range(1, len(report)):
        diff = start - int(report[i])
        if (diff == 0) or (diff < 0 and pole == True) or (diff > 0 and pole == False) or (abs(diff) > 3):
            safe = False
            break
        start = int(report[i])
    if safe:
        numSafe += 1
    else:
        unsafe.append(report)

# 287
print(numSafe)
    
# Part 2
for report in unsafe:
    
    for ignore in range(len(report)):
        cur = report[:ignore] + report[ignore + 1:]
        if all(int(cur[i]) > int(cur[i + 1]) for i in range(len(cur) - 1)) or all(int(cur[i]) < int(cur[i + 1]) for i in range(len(cur) - 1)):
            if all(abs(int(cur[i]) - int(cur[i + 1])) <= 3 for i in range(len(cur) - 1)):
                numSafe += 1
                break
                    

# 354
    

print(numSafe)