"""
Proyecto 2 - Matemática Discreta 1
Sistema de Encriptación RSA

- Bryan Alberto Martínez Orellana 23542
- Adriana Sophia Contreras Palacios 23044
- Javier André Benítez García 23405
"""

import math
import random

#-----------------------------------------Listado de Funciones--------------------------------------------
#------------------------------------------------------------------------------------------------
"""
Función para generar números primos en un rango dado utilizando el test de primalidad de la criba
se obtiene el número, se le saca la raíz, y vemos todos los números primos que le antecedan
tras hacer esto, vemos si dividen al número original, de ser así, es un número compuesto, pero si no pasa
es un número primo y se agrega a la lista para luego pasarle un random.
"""
def generar_primo(rango_inferior, rango_superior):
    
    lista_Primos = []  # Lista para almacenar los primos
    
    # Aseguramos que el rango inferior sea al menos 2, ya que 1 no es primo
    # Si el usuario llega a poner 1 como su límite inferior de una vez le seteamos a 
    if rango_inferior < 2:
        rango_inferior = 2
        
    limite = int(math.sqrt(rango_superior)) 
    primos_menores = criba_eratostenes(limite)

    # Iteramos sobre cada número en el rango definido por el usuario
    for n in range(rango_inferior, rango_superior + 1):
        es_primo = True   # Variable de control marcar si el número es primo (True) o no primo (False)

        # Itera solo sobre los primos hasta la raíz cuadrada de n
        for primo in primos_menores:
            if primo > math.sqrt(n):
                break
            if n % primo == 0:  # Si n es divisible por algún primo, no es primo
                es_primo = False
                break
            
        # Si después del bucle `for` es_primo sigue en True, significa que n es primo
        if es_primo:
            lista_Primos.append(n)  
    
    # Manejo del caso en que no se encuentran números primos en el rango
    if not lista_Primos:
        print("No se encontraron números primos en el rango especificado, por favor amplie el rango de búsqueda.")
        return None  
    
    numb_primo = random.choice(lista_Primos)
    return numb_primo  
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
"""
Función para encontrar el MCD entre dos números utilizando el algoritmo de Euclides
"""
def mcd(a, b):
    try:
        #Verificación de que es un número entero positivo
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Lamentablemente se envío en los parámetros algo que no era un entero.")
        
        #Si alguno de los dos números llegase a ser 0 manejamos el caso devolviendo el
        #número que sea distinto de 0
        if(a == 0 or b == 0):
            return a if a != 0 else b
        
        #El bucle continúa hasta que el residuo entre a y b sea 0
        #Esto ya implicaría que hemos sacado el mcd, el cual sería el residuo de la iteración anterior
        while a % b != 0:
            # Se calcula el residuo de a dividido por b.
            r = a % b
            """
            Actualizamos los valores de las variables
            el que era b pasa a ser a
            el que salió como residuo ahora es b.
            
            Repetimos el proceso hasta que el residuo sea 0,
            nuestro punto de identificación que ya tenemos el MCD.
            """
            a = b
            b = r
       
        # Devolvemos 'b', que sería el MCD
        return b
    except ValueError as e:
        print(e)
        return None
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
"""
Función para encontrar el inverso modular entre el exponente público y n
donde se espera que este n sea el totiente del resultado entre p y q.

En el sistema RSA, utilizamos esto para encontrar la clave privada
para lograrlo se deve calcular el inverso de la 'e' con el módulo del 
totiente de n.
"""
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
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------    
"""
Esta función no está entre la lsita de las funciones solicitadas pero la hemos implementado 
para poder hacer un test de primalidad a la hora de generar un número primo de manera aleatoria, 
más que todo para garantizar que la lista de números generada sea de primos para después parasarle el 
random.
"""
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
#------------------------------------------------------------------------------------------------    

#------------------------------------------------------------------------------------------------    
"""
En esta función es donde ya logramos manejar el flujo completo de lo que se hace en el sistema RSA
La selección de los 2 números primos para generar el 'n', la selección del exponente público 'e',
y el cálculo de la llave privada haciendo uso del inverso modular.
"""
def generar_llaves(rango_inferior, rango_superior):
    # Genera la lista de números primos en el rango especificado
    primo1 = generar_primo(rango_inferior, rango_superior)

    primo2 = primo1
    while primo2 == primo1:
        primo2 = generar_primo(rango_inferior, rango_superior)

    p = primo1
    q = primo2
    
    print(f"Valores de p y q seleccionados: p={p}, q={q}")

    # Calcula n como el producto de p y q
    n = p * q
    
    # Calcula phi(n) = (p - 1) * (q - 1), que se utiliza en la generación de la clave pública y privada
    phi = (p - 1) * (q - 1) #Esto es válido pues al ser dos números primos, el totiente de un número primo, es el número menos 1

    # Aumentamos el valor de la clave hasta que sepamos que el 'e' es corpimo con el totiente de 'n'
    e = 2
    numbListo = False
    while(not numbListo):
        if(mcd(e, phi) == 1):
            numbListo = True
        else:
            e = e + 1
    
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
#------------------------------------------------------------------------------------------------    

#------------------------------------------------------------------------------------------------    
"""
Función para encriptar un carácter utilizando la llave pública,
se recibe el carácter y se convierte a un número utilizando ASCII, 
pero el número asignado al carácter debe ser un número que esté entre 0 y n-1,
ya con este número, se eleva al valor del exponente público 'e' y se le saca el 
módulo n.
"""
def encriptar(caracter, llave_publica):
    numb_ASCII = ord(caracter)
    if(numb_ASCII > llave_publica[1]):
        print("Lamentablemente el 'n' generado es más pequeño que el valor en ASCII de uno de tus carácteres.")
        return None
    
    #Aplicamos la fórmula C=M^e mod n
    mensaje_cifrado = pow(numb_ASCII, llave_publica[0], llave_publica[1])
    return mensaje_cifrado 
#------------------------------------------------------------------------------------------------    

#------------------------------------------------------------------------------------------------    
"""
Función para desencriptar una carácter,
se recibe el carácter que fue cifrado anteriormente, y se eleva al valor de la 
llave privada 'd', para posteriormente aplicarle el mod 'n', y se esperaría
que el resultado de esta operación sea el número correspondiente al carácter
original.
"""
# Función para desencriptar un caracter que se haya encriptado con ayuda de una llave privada
def desencriptar(caracter_encriptado, llave_privada):
    mensaje_descifrado = pow(caracter_encriptado, llave_privada[0], llave_privada[1])
    return mensaje_descifrado
#---------------------------------------------------------------------------------------------------------

#--------------------------Main------------------------
"""
En esta función llevaremos a cabo todo el proceso para el sistema RSA.
Solicitaremos los límites para buscar primos, luego le daremos el menú de opciones 
al usuario, donde podrá salir del programa, o meter una cadena de texto.

En caso de irse por la primera opción, usando los límites definidos se llevará
todo el proceso necesario para encriptar cada uno de los carácteres en la cadena de texto
para luego descifrarlos y así demostrar la válidez del programa, al finalizar
regresa al menú principal.
"""
def main():
    # Solicitar al usuario los límites para generar los números primos
    while True:
        try:
            rango_inferior = int(input("Ingrese el límite inferior para la generación de números primos (debe ser mayor a 1): "))
            rango_superior = int(input("Ingrese el límite superior para la generación de números primos (debe ser mayor a 1): "))
            if rango_inferior <= 1 or rango_superior <= 1:
                print("Ambos límites deben ser mayores a 1. Por favor, intente nuevamente.")
            elif rango_inferior >= rango_superior:
                print("El límite inferior debe ser menor que el límite superior. Por favor, intente nuevamente.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese valores enteros válidos.")



    # Generar las claves RSA
    claves_generadas = generar_llaves(rango_inferior, rango_superior)
    if claves_generadas is None:
        print("Error al generar las claves. El programa terminará.")
        return
    else:
        clave_publica, clave_privada = claves_generadas

    while True:
        print("\n----------------------------Menú-------------------------------")
        print("1. Ingresar cadena de texto")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            texto = input("Por favor, ingresar una cadena de texto: \n")
            
            texto_cifrado = []
            texto_descifrado = []
            
            for caracter in texto:
                print(f"\nProcesando carácter: '{caracter}'")
                
                # Encriptar el carácter
                cifrado = encriptar(caracter, clave_publica)
                if cifrado is None:
                    print("Error en la encriptación. El programa terminará.")
                    return
                
                print(f"Carácter encriptado: {cifrado}")
                
                texto_cifrado.append(cifrado)
                
                # Desencriptar el carácter
                descifrado_num = desencriptar(cifrado, clave_privada)
                caracter_descifrado = chr(descifrado_num)
                
                print(f"Carácter desencriptado: '{caracter_descifrado}'")
                
                texto_descifrado.append(caracter_descifrado)
            # Mostrar los resultados
            print("\nTexto cifrado:")
            print(' '.join(map(str, texto_cifrado)))
            print("Texto descifrado:")
            print(''.join(texto_descifrado))
            
        elif opcion == '2':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
#---------------------------------------------------------------------------------------------------------

main()
