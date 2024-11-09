#Encriptación de un carácter usando la llave pública RSA
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

print(encriptar(20, (3, 253)))