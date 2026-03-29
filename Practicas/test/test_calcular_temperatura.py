import pytest
from practica1.calcular_temperatura import calcular_temperatura

def test_temperatura_frio():
    # PE1: <= 15
    assert calcular_temperatura(10) == "Frío"
    assert calcular_temperatura(-200) == "Frío"

def test_temperatura_templado():
    # PE2: 16 a 25
    assert calcular_temperatura(16) == "Templado"
    assert calcular_temperatura(20) == "Templado"
    assert calcular_temperatura(25) == "Templado"

def test_temperatura_caliente():
    # PE3: > 25
    assert calcular_temperatura(30) == "Caliente"
    assert calcular_temperatura(5000) == "Caliente"

def test_temperatura_fuera_rango_inferior():
    # PE4: < -273
    with pytest.raises(ValueError):
        calcular_temperatura(-274)

def test_temperatura_fuera_rango_superior():
    # PE5: > 10000
    with pytest.raises(ValueError):
        calcular_temperatura(12000)

def test_temperatura_tipo_invalido():
    # PE6: No es int
    with pytest.raises(TypeError):
        calcular_temperatura("calorcito")
    with pytest.raises(TypeError):
        calcular_temperatura(25.5)