X = [
    [1, 2, 3, 1],
    [4, 5, 6, 0],
    [7, 8, 9, -1]
]

transpuesta = list(map(list, zip(*X)))

print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)
