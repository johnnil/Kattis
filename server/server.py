import sys
import math

first_line = sys.stdin.readline().split()
nb_upcoming = int(first_line[0])
kernels_per_machine = int(first_line[1])
last_possible_order = 100000
process_time = 1000

# Set up a timeline of when a machine kernel is needed and when a machine kernel becomes available again
instructions_at_time = [0 for _ in range(last_possible_order+process_time+1)]

# Mark each instruction on the timeline
for i in range(nb_upcoming):
    timestamp = int(sys.stdin.readline())
    instructions_at_time[timestamp] += 1
    instructions_at_time[timestamp+process_time] -= 1

kernels_active = 0
max_kernels_active = 0
for instructions in instructions_at_time:
    kernels_active += instructions
    max_kernels_active = max(max_kernels_active, kernels_active)

nb_servers = math.ceil(max_kernels_active / kernels_per_machine)
print(nb_servers)