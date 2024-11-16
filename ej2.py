lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Potencia n-ésima 
n = 3  

# Usamos una función lambda dentro de map para calcular la potencia n-ésima
potencias = list(map(lambda x: x**n, lista))

print("Lista de potencias:", potencias)
