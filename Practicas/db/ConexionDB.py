# archivo: db.py (o ConexionDB.py)

import psycopg2
from typing import Any
from psycopg2.extensions import connection as PGConnection

class ConexionDB:
    def __init__(
        self,
        host: str,
        database: str,
        user: str,
        password: str,
        port: int = 5432
    ) -> None:
        """Inicializa los parámetros de conexión."""
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self._conn: PGConnection | None = None

    # ----------------------------------
    # Conexión
    # ----------------------------------
    def abrir_conexion(self) -> None:
        """Abre la conexión a la base de datos."""
        try:
            self._conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            print("Conexión establecida con éxito.")
        except Exception as e:
            print(f"Error al conectar: {e}")

    def cerrar_conexion(self) -> None:
        """Cierra la conexión a la base de datos."""
        if self._conn:
            self._conn.close()
            self._conn = None
            print("Conexión cerrada.")

    def _validar_conexion(self) -> None:
        """Verifica que la conexión esté abierta."""
        if self._conn is None:
            raise RuntimeError("La conexión no está abierta. Llama a 'abrir_conexion()' primero.")

    # ----------------------------------
    # CRUD
    # ----------------------------------
    def insertar_empleado(
        self,
        identificador: int,
        nombre: str,
        fecha_nacimiento: str,
        puesto: int,
        sueldo_mensual: float
    ) -> None:
        """Inserta un empleado en la base de datos."""
        self._validar_conexion()
        # CAMBIO APLICADO: 'id' cambiado a 'id_empleado'
        query = "INSERT INTO empleados (identificador, nombre, fecha_nacimiento, puesto, sueldo_mensual) VALUES (%s, %s, %s, %s, %s)"
        with self._conn.cursor() as cursor:
            cursor.execute(query, (identificador, nombre, fecha_nacimiento, puesto, sueldo_mensual))
        self._conn.commit()

    def actualizar_sueldo(
        self,
        id_empleado: int,
        nuevo_sueldo: float
    ) -> None:
        """Actualiza el sueldo de un empleado."""
        self._validar_conexion()
        # CAMBIO APLICADO: 'WHERE id =' cambiado a 'WHERE id_empleado ='
        query = "UPDATE empleados SET sueldo_mensual = %s WHERE identificador = %s"
        with self._conn.cursor() as cursor:
            cursor.execute(query, (nuevo_sueldo, identificador))
        self._conn.commit()

    def eliminar_empleado(self, identificador: int) -> None:
        """Elimina un empleado por ID."""
        self._validar_conexion()
        # CAMBIO APLICADO: 'WHERE id =' cambiado a 'WHERE id_empleado ='
        query = "DELETE FROM empleados WHERE identificador = %s"
        with self._conn.cursor() as cursor:
            cursor.execute(query, (identificador,))
        self._conn.commit()

    def consultar_empleados(self) -> list[tuple]:
        """Retorna una lista de empleados."""
        self._validar_conexion()
        query = "SELECT * FROM empleados"
        with self._conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()