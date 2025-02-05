import re

WIDE = 101
TALL = 103

# Parse input data
def parse():
    f = open("day14_input.txt")
    bot_info = []
    for line in f:
        line_info = re.findall(r"-?\d+", line)
        bot_info.append(list(map(int, line_info)))
    return bot_info

def print_map(bathroom, sec):
    f = open(f"day14_output{sec}.txt", "w")
    for i in range(len(bathroom)):
        for j in range(len(bathroom[0])):
            if bathroom[i][j] == 0:
                f.write(".")
            else:
                f.write("X")
        f.write("\n")
    f.write("\n\n\n")

def calc_quad(bot_info):
    quadrants = [0, 0, 0, 0]
    bathroom = []
    for r in range(TALL):
        bathroom.append(list(0 for c in range(WIDE)))

    for bot in bot_info:
        # Calculate Final location after 100 seconds
        finaly = (bot[1] + bot[3] * 100) % TALL
        finalx = (bot[0] + bot[2] * 100) % WIDE
        bathroom[finaly][finalx] += 1
        # Determine quadrant of the final location
        mid_y = TALL // 2
        mid_x = WIDE // 2
        if finaly != mid_y and finalx != mid_x:
            if finaly < mid_y and finalx < mid_x:
                quadrants[0] += 1
            elif finaly < mid_y and finalx > mid_x:
                quadrants[1] += 1
            elif finaly > mid_y and finalx < mid_x:
                quadrants[2] += 1
            elif finaly > mid_y and finalx > mid_x:
                quadrants[3] += 1
    
    print_map(bathroom, 0)
    return quadrants

# Find the hidden christmas tree
def find_easter_egg(bot_info):

    for sec in range(1, 10000):
        bathroom = []
        for r in range(TALL):
            bathroom.append(list(0 for c in range(WIDE)))
        for i in range(len(bot_info)):
            x = (bot_info[i][0] + bot_info[i][2] * sec) % WIDE
            y = (bot_info[i][1] + bot_info[i][3] * sec) % TALL
            bathroom[y][x] += 1
            
            if (sec - 76) % 103 == 0:
                print_map(bathroom, sec)
    # 6771
        



            


def main():
    bot_info = parse()
    quadrants = calc_quad(bot_info)
    safety_score = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    # 231221760
    print(safety_score)

    find_easter_egg(bot_info)

    


if __name__ == "__main__":
    main()
    