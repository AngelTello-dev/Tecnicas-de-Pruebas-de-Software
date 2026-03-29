import pytest
from practica1.clasificar_calificacion import clasificar_calificacion

def test_calificacion_reprobado():
    # PE1: < 6
    assert clasificar_calificacion(5.9) == "Reprobado"
    assert clasificar_calificacion(0) == "Reprobado"

def test_calificacion_aprobado():
    # PE2: 6 a < 9
    assert clasificar_calificacion(6) == "Aprobado"
    assert clasificar_calificacion(7.5) == "Aprobado"
    assert clasificar_calificacion(8.9) == "Aprobado"

def test_calificacion_sobresaliente():
    # PE3: 9 a 10
    assert clasificar_calificacion(9) == "Sobresaliente"
    assert clasificar_calificacion(10) == "Sobresaliente"

def test_calificacion_fuera_rango_inferior():
    # PE4: < 0
    with pytest.raises(ValueError):
        clasificar_calificacion(-1)

def test_calificacion_fuera_rango_superior():
    # PE5: > 10
    with pytest.raises(ValueError):
        clasificar_calificacion(11)

def test_calificacion_tipo_invalido():
    # PE6: No es numérico
    with pytest.raises(TypeError):
        clasificar_calificacion("9")
    with pytest.raises(TypeError):
        clasificar_calificacion([8, 9])