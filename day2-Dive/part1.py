# input_file_name = "sample_input.txt"
input_file_name = "input.txt"

position = (0, 0)
with open(input_file_name) as input_file:
    for line in input_file.readlines():
        line = line.strip()
        direction, amount = line.split()

        if direction == "forward":
            position = (position[0] + int(amount), position[1])
        elif direction == "down":
            position = (position[0], position[1] - int(amount))
        elif direction == "up":
            position = (position[0], position[1] + int(amount))
        else:
            raise Exception(f"Undespected direction {direction}")

print(f"Result {position[0] * position[1] * -1}")
