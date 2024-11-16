def ejercicio1():
    D = [
        {'make': 'Nokia', 'model': 216, 'color': 'Black'},
        {'make': 'Apple', 'model': 2, 'color': 'Silver'},
        {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
    ]

    # Ordenar la lista de diccionarios por la clave 'model' usando lambda
    D_sorted = sorted(D, key=lambda x: x['model'])

    print("Lista antes: ")
    for item in D:
        print(item)

    print("Lista ordenada:")
    for item in D_sorted:
        print(item)
