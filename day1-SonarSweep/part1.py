import sys

# input_file_name = "sample_input.txt"
input_file_name = "input.txt"

depth_increases = 0
previous_depth = None
with open(input_file_name) as input_file:
    for line in input_file.readlines():
        line = line.strip()
        
        depth = int(line)

        if depth > (previous_depth or sys.maxsize):
            depth_increases = depth_increases + 1
        
        previous_depth = depth

print(f"Increases: {depth_increases}")