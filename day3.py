import re

f = open("day3_input.txt")
text = f.read()
validInstructions = re.findall(r"mul\(\d+,\d+\)", text)

total = 0
for inst in validInstructions:
    values = re.findall(r"\d+", inst)
    total += int(values[0]) * int(values[1])

# 188741603
print(total)

# Part 2
validInstructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", text)

total = 0
allowMult = True
for inst in validInstructions:
    if inst == "don't()":
        allowMult = False
    elif inst == "do()":
        allowMult = True
    else:
        if allowMult:
            values = re.findall(r"\d+", inst)
            total += int(values[0]) * int(values[1])

# 67269798
print(total)