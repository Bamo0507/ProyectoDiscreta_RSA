"""
Proyecto 2 - Matemática Discreta 1
Sistema de Encriptación RSA

- Bryan Alberto Martínez Orellana 23542
- Adriana Sophia Contreras Palacios 23044
- Javier Andrés Benítez García 23405
"""

import math
import random

#-----------------------------------------Listado de Funciones--------------------------------------------

#Función para generar números primos en un rango dado utilizando la Criba y el método de división de prueba
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

# Función para encontrar el máximo común divisor entre dos números 'a' y 'b' utilizando el algoritmo euclidiano
def mcd(a, b):
    try:
        #Verificación de que es un número entero positivo
        if not isinstance(a, int) and not isinstance(b, int):
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
    
# Función para encontrar el inverso modular entre el exponente público y n
# En el inverso modular encontramos un número que al multiplicarlo por 'e', sea congruente a 1 mod n
def inverso_modular(e, n):
    try:
        # Aqui se verifica que ambos sean enteros positivos
        if not isinstance(e, int) or not isinstance(n, int):
            raise ValueError("Error: Ambos parámetros deben ser enteros.")
        if e <= 0 or n <= 0:
            raise ValueError("Error: Ambos parámetros deben ser enteros positivos.")

        #  residuos y coeficientes necesarios para el cálculo
        r0, r1 = n, e  # Residuos iniciales
        s0, s1 = 1, 0  # Coeficientes para calcular el inverso

        # Algoritmo extendido de Euclides
        while r1 != 0:
            q = r0 // r1  # Calcula el cociente de la división
            r0, r1 = r1, r0 - q * r1  
            s0, s1 = s1, s0 - q * s1  

       # si el MCD es igual a 1 significa que si hay inverso modular 

        if r0 == 1:
            return s0 % n  
        else:
            return None  # No hay inverso modular si el MCD no es 1

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


# Función para generar las llave pública y privada para el algoritmo RSA 

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

# Función para encriptar un mensaje dado el caracter a encriptar, y la llave pública
def encriptar(caracter, llave_publica):
    ##Validaciones para el carácter
    try:
        ##Veficar que el carácter sea un número entero positivo
        if not isinstance(caracter, int) or caracter <= 0:
            raise ValueError("Lamentablemente el carácter que has ingresado no es un entero positivo.")
        ##Verificar que el carácter sea menor que n
        if caracter >= llave_publica[1]:
            raise ValueError("El carácter que has seleccionado es mayor al valor del módulo.")
        
        ##Se usa la fórmula C=M^e, e es el exponente público
        C = caracter**llave_publica[0]
        
        ##Se saca la función módulo de C mod n 
        mensaje_cifrado = C % llave_publica[1]
        return mensaje_cifrado  
    
    except ValueError as e:
        ##Impresión de cualquier error que se pueda llegar a levantar
        print(e)
        return None    
    
# Función para desencriptar un caracter que se haya encriptado con ayuda de una llave privada
def desencriptar(caracter_encriptado, llave_privada):
    try:
        #Verificación de que es un número entero positivo
        if not isinstance(caracter_encriptado, int) and caracter_encriptado <= 0:
            raise ValueError("Lamentablemente el carácter que has ingresado no es un entero positivo.")
        if caracter_encriptado >= llave_privada[1]:
            raise ValueError("El carácter que has seleccionado es mayor al valor del módulo.")
        ##Se usa la fórmula M=C^d, d es la clave privada
        M = caracter_encriptado**llave_privada[0]
        
        ##Se saca la función módulo de M mod n
        mensaje_cifrado = M % llave_privada[1]
        return mensaje_cifrado  
    except ValueError as e:
        print(e)
        return None
#---------------------------------------------------------------------------------------------------------

