# archivo: main.py

from ConexionDB import ConexionDB


def main() -> None:
    # 1. Crear el objeto
    db = ConexionDB(
        host="localhost",
        database="sistema_abc",
        user="uacm",
        password="uacm1"
    )

    # 2. Abrir la conexión explícitamente
    db.abrir_conexion()

    try:
        # ----------------------------
        # Insertar empleados (ID manual)
        # ----------------------------
        print("\n--- Insertando empleados ---")
        db.insertar_empleado(1, "Juan Pérez", "1990-05-10", 1, 15000.50)
        db.insertar_empleado(2, "Ana López", "1985-08-20", 2, 18000.75)

        # ----------------------------
        # Consultar
        # ----------------------------
        empleados = db.consultar_empleados()
        print("\nEmpleados iniciales:")
        for emp in empleados:
            print(emp)

        # ----------------------------
        # Actualizar sueldo
        # ----------------------------
        print("\n--- Actualizando sueldo del ID 1 ---")
        db.actualizar_sueldo(1, 20000.00)

        # ----------------------------
        # Eliminar empleado
        # ----------------------------
        print("--- Eliminando empleado con ID 2 ---")
        db.eliminar_empleado(2)

        # ----------------------------
        # Consultar nuevamente
        # ----------------------------
        empleados = db.consultar_empleados()
        print("\nEmpleados después de cambios:")
        for emp in empleados:
            print(emp)

    finally:
        # 3. Cerrar conexión siempre (incluso si hay errores arriba)
        print("\n--- Limpieza ---")
        db.cerrar_conexion()


if __name__ == "__main__":
    main()