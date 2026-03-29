def calcular_temperatura(temperatura):
    # Validar que sea un número entero (excluyendo booleanos que en Python heredan de int)
    if type(temperatura) is not int:
        raise TypeError("El valor debe ser un número entero.")
    
    # Validar los rangos extremos
    if temperatura < -273 or temperatura > 10000:
        raise ValueError("La temperatura está fuera del rango válido (-273 a 10000).")
        
    # Clasificación
    if temperatura <= 15:
        return "Frío"
    elif 16 <= temperatura <= 25:
        return "Templado"
    else:
        return "Caliente"