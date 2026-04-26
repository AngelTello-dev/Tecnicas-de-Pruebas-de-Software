# test_producto.py
import pytest
from Practica2.producto import (
    Producto,
    NombreVacioProductoError,
    NombreProductoError,
    PrecioRangoError,
    PrecioInvalidoError,
)

# ---------- Fixtures ----------
@pytest.fixture
def producto_valido():
    """Producto básico para pruebas que no verifican el constructor."""
    return Producto("Test", 100.0)

# ---------- Pruebas de constructor ----------
@pytest.mark.parametrize("nombre, precio, esperado", [
    # PE y VL combinados
    ("", 100.0, NombreVacioProductoError),                    # T1, VL1
    ("A"*51, 100.0, NombreProductoError),                    # T2, VL4
    (123, 100.0, NombreProductoError),                       # T3
    ("Lápiz", 5.50, None),                                   # T4, válido
])
def test_constructor_nombre(nombre, precio, esperado):
    if esperado:
        with pytest.raises(esperado):
            Producto(nombre, precio)
    else:
        p = Producto(nombre, precio)
        assert p.nombre == nombre
        assert p.precio == precio

@pytest.mark.parametrize("nombre, precio, esperado", [
    ("X", "100", PrecioInvalidoError),                       # T5
    ("X", -5.50, PrecioRangoError),                          # T6, VL5
    ("X", 0.0, PrecioRangoError),                            # VL6
    ("X", 2000000.01, PrecioRangoError),                     # T7, VL10
])
def test_constructor_precio_invalido(nombre, precio, esperado):
    with pytest.raises(esperado):
        Producto(nombre, precio)

@pytest.mark.parametrize("precio", [
    0.01, 1.0, 500.0, 2000000.0, 1999999.99,               # VL7, VL8, VL9, ...
])
def test_constructor_precio_valido(precio):
    p = Producto("X", precio)
    assert p.precio == round(precio, 2)

# ---------- Pruebas de calcular_descuento ----------
@pytest.mark.parametrize("precio, descuento_esperado", [
    (250.0, 0.0),
    (499.99, 0.0),        # VL11
    (500.0, 0.0),         # VL12
    (500.01, 25.0),       # VL13  (500.01*0.05=25.0005 -> 25.0)
    (1000.0, 50.0),
    (1999.99, 100.0),     # VL14  (1999.99*0.05=99.9995 -> 100.0)
    (2000.0, 100.0),      # VL15
    (2000.01, 200.0),     # VL16  (2000.01*0.1=200.001 -> 200.0)
    (10000.0, 1000.0),
    (29999.99, 3000.0),   # VL17  (29999.99*0.1=2999.999 -> 3000.0)
    (30000.0, 3000.0),    # VL18
    (30000.01, 4500.0),   # VL19  (30000.01*0.15=4500.0015 -> 4500.0)
    (50000.0, 7500.0),
])
def test_calcular_descuento(precio, descuento_esperado):
    p = Producto("P", precio)
    assert p.calcular_descuento() == descuento_esperado

# ---------- Pruebas de precio_final ----------
def test_precio_final(producto_valido):
    # producto_valido: precio=100 -> sin descuento, final=100
    assert producto_valido.precio_final() == 100.0

@pytest.mark.parametrize("precio, final_esperado", [
    (500.0, 500.0),
    (500.01, 475.01),    # 500.01 - 25.00 = 475.01
    (2000.0, 1900.0),
    (30000.0, 27000.0),
    (30000.01, 25500.01), # 30000.01 - 4500.00 = 25500.01
])
def test_precio_final_varios(precio, final_esperado):
    p = Producto("Y", precio)
    assert p.precio_final() == final_esperado