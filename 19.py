# Dataset: Sekwencja stanów
states = ["A", "B", "A", "A", "C", "B", "C", "A", "B", "B"]

unique_states = sorted(list(set(states)))

transition_matrix = {start: {end: 0 for end in unique_states} for start in unique_states}


for i in range(len(states) - 1):
    current_state = states[i]
    next_state = states[i + 1]


    transition_matrix[current_state][next_state] += 1

print("Macierz przejść (Z -> DO):")

header = "     " + "  ".join([f"{s:>3}" for s in unique_states])
print(header)
print("-" * len(header))

for start_node in unique_states:
    row_str = f"{start_node:>3} |"
    for end_node in unique_states:
        count = transition_matrix[start_node][end_node]
        row_str += f"{count:>5}"
    print(row_str)
