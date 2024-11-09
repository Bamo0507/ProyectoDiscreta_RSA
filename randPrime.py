import math
import random

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

# Función para generar números primos en un rango dado utilizando la Criba y el método de división de prueba
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
    
    return lista_Primos  

# Nueva función para calcular el inverso modular usando el algoritmo extendido de Euclides
def inverso_modular(e, n):
    try:
        if not isinstance(e, int) or not isinstance(n, int):
            raise ValueError("Error: Ambos parámetros deben ser enteros.")
        if e <= 0 or n <= 0:
            raise ValueError("Error: Ambos parámetros deben ser enteros positivos.")

        r0, r1 = n, e
        s0, s1 = 1, 0

        while r1 != 0:
            q = r0 // r1
            r0, r1 = r1, r0 - q * r1  
            s0, s1 = s1, s0 - q * s1  

        if r0 == 1:
            return s0 % n  
        else:
            return None

    except ValueError as e:
        print(e)
        return None

def inverso_modular(e, n):
    try:
        if not isinstance(e, int) or not isinstance(n, int):
            raise ValueError("Error: Ambos parámetros deben ser enteros.")
        if e <= 0 or n <= 0:
            raise ValueError("Error: Ambos parámetros deben ser enteros positivos.")

        r0, r1 = n, e
        s0, s1 = 1, 0

        while r1 != 0:
            q = r0 // r1
            r0, r1 = r1, r0 - q * r1  
            s0, s1 = s1, s0 - q * s1  

        if r0 == 1:
            return s0 % n  
        else:
            return None

    except ValueError as e:
        print(e)
        return None


def generar_llaves(rango_inferior, rango_superior):
    # Genera la lista de números primos en el rango especificado
    primos = generar_primo(rango_inferior, rango_superior)
    
    # Si no se encontraron suficientes números primos, se muestra un mensaje de error y se retorna None
    if primos is None or len(primos) < 2:
        print("No se encontraron suficientes números primos en el rango especificado.")
        return None

    # Selecciona dos primos aleatorios diferentes de la lista de primos generados
    p, q = random.sample(primos, 2)
    print(f"Valores de p y q seleccionados: p={p}, q={q}")

    # Calcula n como el producto de p y q
    n = p * q
    
    # Calcula phi(n) = (p - 1) * (q - 1), que se utiliza en la generación de la clave pública y privada
    phi = (p - 1) * (q - 1)

    # Inicializa e en 2, que es el valor que se utilizará en la clave pública
    e = 2
    
    # Busca un valor de e tal que sea coprimo con phi(n), es decir, gcd(e, phi) == 1
    # Se incrementa e hasta encontrar un valor válido o hasta que e sea mayor o igual a phi(n)
    while e < phi and math.gcd(e, phi) != 1:
        e += 1
    
    # Si no se encontró un valor válido de e, se muestra un mensaje de error y la función retorna None
    if e >= phi:
        print("No se pudo encontrar un valor válido para e.")
        return None

    # Calcula el inverso modular de e con respecto a phi(n), que será d
    d = inverso_modular(e, phi)
    
    # Si no se pudo calcular el inverso modular, se muestra un mensaje de error y se retorna None
    if d is None:
        print("No se pudo calcular el inverso modular de e, intente con otro rango.")
        return None

    # Si e y d son iguales, se muestra un mensaje de error porque deben ser diferentes
    if e == d:
        print("No se pudo generar un par de claves válidas donde e y d sean diferentes.")
        return None

    # Genera la clave pública como una tupla (e, n)
    clave_publica = (e, n)
    
    # Genera la clave privada como una tupla (d, n)
    clave_privada = (d, n)
    
    # Imprime las claves generadas
    print(f"Clave Pública: {clave_publica}")
    print(f"Clave Privada: {clave_privada}")

    # Retorna las claves pública y privada como una tupla
    return clave_publica, clave_privada

# Llamada a la función con un rango de números primos entre 10 y 50
generar_llaves(10, 50)