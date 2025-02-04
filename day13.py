from math import gcd, floor, ceil

f = open("day13_input.txt")

a_buttons = []
b_buttons = []
prizes = []
PRICE_A = 3
PRICE_B = 1

# Parse Input
for line in f:
    if line.find("Button A: ") != -1:
        xy = line.strip("Button A: ").split(",")
        a_buttons.append((int(xy[0].strip("X+")), int(xy[1].strip(" Y+\n"))))
    elif line.find("Button B: ") != -1:
        xy = line.strip("Button B: ").split(",")
        b_buttons.append((int(xy[0].strip("X+")), int(xy[1].strip(" Y+\n"))))
    elif line.find("Prize: ") != -1:
        xy = line.strip("Prize: ").split(",")
        prizes.append((int(xy[0].strip("X=")), int(xy[1].strip(" Y=\n"))))

def lde(a, b, c):
    # From https://new.math.uiuc.edu/public348/python/diophantus.html
    q, r = divmod(a, b)
    if r == 0:
        return ([0, c/b])
    else:
        sol = lde(b, r, c)
        u = sol[0]
        v = sol[1]
        return ([v, u-q*v])


def find_prize(prize, a, b):
    memo = []
    for i in range(101):
        memo.append(list(0 for x in range(101)))
    
    for row in range(101):
        for col in range(101):
            if row == 0 and col == 0:
                memo[row][col] = 0
            elif row > 0 and col == 0:
                memo[row][col] = 3 + memo[row - 1][col]
            elif row == 0 and col > 0:
                memo[row][col] = 1 + memo[row][col - 1]
            else:
                memo[row][col] = min(3 + memo[row - 1][col], 1 + memo[row][col - 1])
            x = row * a[0] + col * b[0]
            y = row * a[1] + col * b[1]
            if (x, y) == prize:
                return memo[row][col], True
    return 0, False

def price(ax, ay, bx, by, tx, ty):
    det = ax*by - bx*ay
    if det != 0:
        # Case 1: Only one possible solution
        aDet = tx*by - ty*bx
        bDet = ty*ax - tx*ay
        
        if aDet % det == 0 and bDet % det == 0:
            # The solution is valid only A and B are integers
            A, B = aDet//det, bDet//det
            return PRICE_A*A + PRICE_B*B
        
        return -1
    
    detAug = ax*ty - tx*ay
    if detAug == 0 and tx % gcd(ax, bx) != 0:
        # Case 2: Many possible solutions, but none are valid
        return -1
    
    # Case 3: Many possible solutions, but only one is optimal
    # Find one solution to the LDE: A(ax) + B(bx) = tx
    A0, B0 = lde(ax, bx, tx)
    
    # General solutions are of the form: A = A0 + k*bx, B = B0 - k*ax
    # Select the k that minimizes the cost inefficient button
    k = [ceil(-A0/bx), floor(B0/ax)]
    k = max(k[0], k[1]) if ax/bx > PRICE_A else min(k[0], k[1])
    
    A = A0+k*bx
    B = B0-k*ax
    
    if A < 0 or B < 0:
        # Invalid solution, despite selecting optimal k
        return -1
    
    return PRICE_A*A + PRICE_B*B

total_tokens = 0
part2_tokens = 0
for i in range(len(prizes)):
    #tokens, found = find_prize(prizes[i], a_buttons[i], b_buttons[i])
    #if found:
    #    total_tokens += tokens


    # https://www.reddit.com/r/adventofcode/comments/1i20wpg/2024_day_13_what_if_the_buttons_are_linearly/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1
    a = a_buttons[i][0]
    b = b_buttons[i][0]
    c = a_buttons[i][1]
    d = b_buttons[i][1]

    px = prizes[i][0]
    py = prizes[i][1]
    cost = price(a, c, b, d, px, py)
    if cost > 0:
        total_tokens += cost
    second_cost = price(a, c, b, d, px +10000000000000, py + 10000000000000)
    if second_cost > 0:
        part2_tokens += second_cost

    
# 39290
print(total_tokens)

# 73458657399094
print(part2_tokens)