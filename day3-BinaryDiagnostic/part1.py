import typing as typ

# input_file_name = "sample_input.txt"
input_file_name = "input.txt"

from collections import Counter

bits: typ.List[typ.List[str]] = []

with open(input_file_name) as input_file:
    for line in input_file.readlines():
        line = line.strip()
        
        if len(bits) < len(line):
            for i in range(len(line) - len(bits)):
                bits.append([])

        for i in range(len(bits)):
            bits[i].append(line[i])

gamma_rate = []
for i in range(len(bits)):
    gamma_rate.append(Counter("".join(bits[i])).most_common()[0][0])
    
    # epsilon_rate.append("0" if 

# epsilon_rate = [g for g in gamma_rate]
epsilon_rate = ["0" if int(g) == 1 else "1" for g in gamma_rate]
print("".join(gamma_rate))
print("".join(epsilon_rate))
print(f"Result {int(''.join(gamma_rate), 2) * int(''.join(epsilon_rate), 2)}")