import random
import math

def inverso_modular(e, n):
    # Verificar que ambos sean enteros positivos
    if not isinstance(e, int) or not isinstance(n, int):
        raise ValueError("Error: Ambos parámetros deben ser enteros.")
    if e <= 0 or n <= 0:
        raise ValueError("Error: Ambos parámetros deben ser enteros positivos.")

    # Inicialización de residuos y coeficientes
    a = n
    b = e
    residuo = -1
    cociente = 0
    lista_Cocientes = []
    lista_residuos = []
    lista_A = []
    lista_B = []

    # Algoritmo extendido de Euclides
    while residuo != 0:
        lista_A.append(a)
        lista_B.append(b)
        cociente = a // b
        residuo = a % b
        lista_Cocientes.append(cociente)
        lista_residuos.append(residuo)
        a = b
        b = residuo

    # Si el último residuo no es 1, no existe el inverso modular
    if lista_residuos[-2] != 1:
        raise ValueError("No existe el inverso modular porque los números no son coprimos.")

    # Inicialización de variables que representarán a los coeficientes de Bézout
    x = 1
    y = 0
    x_anterior = 0
    y_anterior = 1

    # Actualización de coeficientes de Bézout usando los cocientes calculados
    for i in range(len(lista_Cocientes)):
        x_actual = x
        x = x_anterior - lista_Cocientes[i] * x
        x_anterior = x_actual

        y_actual = y
        y = y_anterior - lista_Cocientes[i] * y
        y_anterior = y_actual

    # Asegurarse de que x_anterior sea positivo en el rango del módulo
    inverso = x_anterior % n

    return inverso

def mcd(a, b):
    try:
        #Verificación de que es un número entero positivo
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Lamentablemente se envío en los parámetros algo que no era un entero.")
        #El bucle continúa hasta que el residuo entre a y b sea 0
        #Esto ya implicaría que hemos sacado el mcd, el cual sería el residuo de la iteración anterior
        
        #Preguntar a Mario si así se maneja
        if(a == 0 or b == 0):
            return a if a != 0 else b
        
        while a % b != 0:
            # Se calcula el residuo de a dividido por b.
            r = a % b
            a = b
            b = r
            
        # Devolvemos 'b', que sería el MCD
        return b
    
    except ValueError as e:
        print(e)
        return None
    
# Función para generar una lista de números primos usando la Criba de Eratóstenes
def criba_eratostenes(limite):
    # Se crea una lista donde cada índice representa un número; el valor True indica que es primo
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos

    # Comienza desde el primer número primo, 2, y marca todos sus múltiplos como no primos
    for i in range(2, int(math.sqrt(limite)) + 1):
        if es_primo[i]:  # Si i es primo
            for j in range(i * i, limite + 1, i):  # Marca múltiplos de i como no primos
                es_primo[j] = False

    # Devuelve una lista de números primos hasta el límite especificado
    return [p for p, primo in enumerate(es_primo) if primo]

def generar_primo(rango_inferior, rango_superior):
    
    lista_Primos = []  # Se inicializa la lista para almacenar los números primos encontrados
    
    # Aseguramos que el rango inferior sea al menos 2, ya que 1 no es primo
    if rango_inferior < 2:
        rango_inferior = 2

    # Iteramos sobre cada número en el rango definido por el usuario
    for n in range(rango_inferior, rango_superior):
        
        # Calculamos el límite superior de divisores necesarios (la raíz cuadrada de n)
        limite = int(math.sqrt(n))
        
        # Obtenemos todos los números primos menores o iguales a la raíz cuadrada de n
        primos_menores = criba_eratostenes(limite)
        
        es_primo = True  # Variable para marcar si el número es primo (True) o no primo (False)

        # Itera solo sobre los primos hasta la raíz cuadrada de n
        for primo in primos_menores:
            if n % primo == 0:  # Si n es divisible por algún primo, entonces no es primo
                es_primo = False  # Marca que el número no es primo
                break  

        # Si después del bucle `for` es_primo sigue en True, significa que n es primo
        if es_primo:
            lista_Primos.append(n)  
            print(f"Primo: {n}")  
    
    # Manejo del caso en que no se encuentran números primos en el rango
    if not lista_Primos:
        print("No se encontraron números primos en el rango especificado, porfavor amplie el rango de busqueda.")
        return None  
    
    numb_primo = random.choice(lista_Primos)
    
    return numb_primo  

print(inverso_modular(4, 15))