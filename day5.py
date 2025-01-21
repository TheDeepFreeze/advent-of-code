f = open("day5_input.txt")
from collections import defaultdict

text = f.readlines()

ordering = []
updates = []
space = True
for line in text:
    if line == "\n":
        space = False
    else:
        if space:
            ordering.append(line.rstrip("\n"))
        else:
            updates.append(line.rstrip("\n"))

order = defaultdict(list)
for rule in ordering:
    req, page = rule.split("|")
    order[page].append(req)

middle = 0
incorrect = []
for update in updates:
    pages = update.split(",")
    valid = True
    prev = []
    for page in pages:
        reqs = order[page]
        for req in reqs:
            if req in pages and req not in prev:
                valid = False
                break
        if not valid:
            break
        prev.append(page)
    if valid:
        middle += int(pages[len(pages) // 2])
    else:
        incorrect.append(pages)
# 5129
print(middle)

# Part 2
inmiddle = 0
for update in incorrect:
    freqs = {}
    prev = []
    def rec(x, pages):
        reqs = order[x]
        for req in reqs:
            if req in pages and req not in prev:
                rec(req, pages)
                prev.append(req)
    
    for page in update:
        rec(page, update)
    inmiddle += int(prev[len(prev) // 2])
# 4077
print(inmiddle)