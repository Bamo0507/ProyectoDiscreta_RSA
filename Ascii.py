#Función para convertir de texto a ASCII
def texto_ASCII(text):
    return [ord(char) for char in text]

print(texto_ASCII("HOLAAAA"))

def ascii_to_text(ascii_list):
    return ''.join(chr(num) for num in ascii_list)

print(ascii_to_text(texto_ASCII("HOLAAAA")))

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
    
print(mcd(34, 3127))