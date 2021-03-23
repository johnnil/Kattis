import sys

current_position = int(sys.stdin.readline())
target_position = int(sys.stdin.readline())

# Three possibilities
alpha = target_position - current_position
beta = target_position - current_position + 360
gamma = target_position - current_position - 360
paths = [alpha, beta, gamma]
shortest = [abs(alpha), abs(beta), abs(gamma)]
move = paths[shortest.index(min(shortest))]
if move == -180:
    move = 180
print(move)
