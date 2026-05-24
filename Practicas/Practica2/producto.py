# producto.py
class NombreVacioProductoError(Exception):
    """El nombre no puede ser una cadena vacía."""
    pass

class NombreProductoError(Exception):
    """El nombre no puede tener más de 50 caracteres ni ser un valor numérico."""
    pass

class PrecioRangoError(Exception):
    """El precio debe ser > 0 y <= 2,000,000."""
    pass

class PrecioInvalidoError(Exception):
    """El precio no puede ser una cadena de texto."""
    pass


class Producto:
    def __init__(self, nombre, precio):
        # Validación de nombre
        if not isinstance(nombre, str):
            raise NombreProductoError("El nombre no puede ser un valor numérico u otro tipo no cadena.")
        if nombre == "":
            raise NombreVacioProductoError("El nombre no puede estar vacío.")
        if len(nombre) > 50:
            raise NombreProductoError("El nombre no puede exceder los 50 caracteres.")

        # Si es cadena pero representa un número? la especificación dice "valor numérico",
        # interpretamos tipo numérico, no contenido. Dejamos pasar cadenas que parezcan números.
        self.nombre = nombre

        # Validación de precio
        if isinstance(precio, str):
            raise PrecioInvalidoError("El precio no puede ser una cadena de texto.")
        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número (int o float).")
        if precio <= 0 or precio > 2_000_000:
            raise PrecioRangoError("El precio debe estar en el rango (0, 2,000,000].")
        # Redondeamos a 2 decimales para garantizar precisión
        self.precio = round(precio, 2)

    def calcular_descuento(self):
        """Retorna el monto del descuento según el precio."""
        p = self.precio
        if p <= 500:
            descuento = 0.0
        elif p <= 2000:
            descuento = p * 0.05
        elif p <= 30000:
            descuento = p * 0.10
        else:
            descuento = p * 0.15
        return round(descuento, 2)

    def precio_final(self):
        """Retorna el precio con descuento aplicado."""
        return round(self.precio - self.calcular_descuento(), 2)