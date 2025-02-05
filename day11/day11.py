import functools
f = open("day11_input.txt")

def pebbles(blinks, stones):
    for blink in range(blinks):
        newStones = []
        for stone in stones:
            if stone == "0":
                newStones.append("1")
            elif len(stone) % 2 == 0:
                first = stone[:len(stone) // 2]
                second = stone[len(stone) // 2:]
                newStones.append(str(int(first)))
                newStones.append(str(int(second)))
            else:
                newStone = 2024 * int(stone)
                newStones.append(str(newStone))
        stones = newStones
    return stones

stones = f.read().split()
print(stones)
finalStones = pebbles(25, stones)
# 199753
print(len(finalStones))

@functools.lru_cache(maxsize=None)
def recursivePebbles(blinks, stones):
    if blinks == 0:
        return 1
    elif stones == "0":
        return recursivePebbles(blinks - 1, "1")
    elif len(stones) % 2 == 0:
        x = recursivePebbles(blinks - 1, str(int(stones[:len(stones) // 2])))
        y = recursivePebbles(blinks - 1, str(int(stones[len(stones) // 2:])))
        return x + y
    else:
        return recursivePebbles(blinks - 1, str(int(stones) * 2024))

final = 0
for stone in stones:
    final += recursivePebbles(75, stone)
# Part 2
# 239413123020116
print(final)

