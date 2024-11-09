#Desencriptar un caracter encripatado usando una llave privada de RSA
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
    
print(desencriptar(64, (147, 253)))