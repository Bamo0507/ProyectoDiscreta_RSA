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