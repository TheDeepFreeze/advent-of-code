f = open("day7_input.txt")

# Parse
text = f.readlines()
equations = []
answers = []
for line in text:
    tmp = line.split()
    tmp[0] = tmp[0].strip(":")
    answers.append(int(tmp[0]))
    equations.append(tmp[1:])

# Evaluate
res = {}
def eval(i, ans, equation, idx, total):
    if idx == len(equation):
        if total == ans:
            res[i] = ans
        return
    
    eval(i, ans, equation, idx + 1, total + int(equation[idx]))
    eval(i, ans, equation, idx + 1, total * int(equation[idx]))
    # Part 2
    s1 = str(total) + equation[idx]
    eval(i, ans, equation, idx + 1, int(s1))
    

for i in range(len(equations)):
    eval(i, answers[i], equations[i], 1, int(equations[i][0]))

tot = 0
for i, num in res.items():
    tot += num
# 1399219271639
print(tot)

# Part 2
# 275791737999003
