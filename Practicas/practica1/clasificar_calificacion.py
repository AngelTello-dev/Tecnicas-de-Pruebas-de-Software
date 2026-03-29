def clasificar_calificacion(calificacion):
    # Validar que sea numérico (int o float)
    if type(calificacion) not in (int, float):
        raise TypeError("El valor debe ser numérico (entero o decimal).")
        
    # Validar rango de 0 a 10
    if calificacion < 0 or calificacion > 10:
        raise ValueError("La calificación debe estar entre 0 y 10.")
        
    # Clasificación
    if calificacion < 6:
        return "Reprobado"
    elif calificacion < 9:
        return "Aprobado"
    else:
        return "Sobresaliente"