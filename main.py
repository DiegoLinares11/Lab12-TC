import ej1
import ej2
import ej3
import ej4

def main():
    while True:
        print("\nSeleccione el ejercicio que desea ejecutar:")
        print("1. Ordenación de diccionarios")
        print("2. Potencias n-ésimas")
        print("3. Transposición de matrices")
        print("4. Filtrado de listas")
        print("5. Salir")

        opcion = input("Ingrese el número del ejercicio (1-5): ")

        if opcion == '1':
            ej1.ejercicio1()
        elif opcion == '2':
            ej2.ejercicio2()
        elif opcion == '3':
            ej3.ejercicio3()
        elif opcion == '4':
            ej4.ejercicio4()
        elif opcion == '5':
            print("Saliendo del programa.")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
