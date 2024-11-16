lista_inicial = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']

elementos_a_borrar = ['amarillo', 'café', 'blanco']

# Se uso filter y lambda para eliminar los elementos indicados
lista_filtrada = list(filter(lambda x: x not in elementos_a_borrar, lista_inicial))

print("Lista filtrada:", lista_filtrada)
