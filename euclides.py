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