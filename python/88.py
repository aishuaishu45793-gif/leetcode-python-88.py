nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat_list = []

for sublist in nested_list:
    for number in sublist:
        flat_list.append(number)

print("Flattened list:", flat_list)