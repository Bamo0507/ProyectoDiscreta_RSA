def Algoritmo_euclides(a, b):
   

    # El bucle continúa hasta que el residuo (a % b) sea igual a 0.
    while a % b != 0:
        # Se calcula el residuo de a dividido por b.
        r = a % b
        
        
        a = b
        b = r

    # Cuando b es igual a 0, el valor actual de a es el MCD, se retorna b que es el MCD.
    return b


# Se le solicita al usuario que ingrese dos números enteros positivos para a y b.
a = int(input("Ingrese un entero positivo a: "))
b = int(input("Ingrese un entero positivo b: "))


RAlgoritmo = Algoritmo_euclides(a, b)

# Imprime el resultado, que es el MCD de a y b.
print(f"El mcd de {a} y {b} es {RAlgoritmo}")
