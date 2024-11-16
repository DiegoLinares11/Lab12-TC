def ejercicio3():
    X = [
        [1, 2, 3, 1],
        [4, 5, 6, 0],
        [7, 8, 9, -1]
    ]

    transpuesta = list(map(list, zip(*X)))

    print ("Matriz antes: ")
    for fila in X:
        print(fila)

    print("Matriz transpuesta:")
    for fila in transpuesta:
        print(fila)
