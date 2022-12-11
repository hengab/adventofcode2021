import sys
from collections import deque

# input_file_name = "sample_input.txt"
input_file_name = "input.txt"

depth_increases = 0
previous_depths = deque(maxlen=4)
with open(input_file_name) as input_file:
    for line in input_file.readlines():
        line = line.strip()
        
        depth = int(line)
        previous_depths.append([])

        for d in previous_depths:
            d.append(depth)
        # Start measuring once we have four deques
        if len(previous_depths) > 3:
            # print(f"Comparing {sum(previous_depths[0][0:3])} < {sum(previous_depths[1])} ({sum(previous_depths[0][0:3]) < sum(previous_depths[1])})")
            if sum(previous_depths[0][0:3]) < sum(previous_depths[1]):
                depth_increases = depth_increases + 1
        

print(f"Increases: {depth_increases}")