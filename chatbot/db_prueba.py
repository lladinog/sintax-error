import mysql.connector
from mysql.connector import Error

def crear_base_datos_y_tabla():
    try:
        # Conexión sin especificar la base de datos (para poder crearla)
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",          # Cambia esto si usas otro usuario
            password="@CP2006-Maths"  # Cambia esto por tu contraseña real
        )

        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS test_db;")
            cursor.execute("USE test_db;")

            # Crear tabla users
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    age INT,
                    email VARCHAR(100)
                );
            """)

            # Insertar datos de prueba
            cursor.execute("DELETE FROM users;")  # Limpieza previa
            cursor.executemany("""
                INSERT INTO users (name, age, email)
                VALUES (%s, %s, %s)
            """, [
                ("Ana Pérez", 25, "ana@example.com"),
                ("Juan Gómez", 17, "juan@example.com"),
                ("Laura Ruiz", 32, "laura@example.com"),
                ("Carlos Méndez", 19, "carlos@example.com")
            ])

            conexion.commit()
            print("✅ Base de datos y tabla 'users' creadas con datos de prueba.")
    
    except Error as e:
        print(f"❌ Error al crear base de datos: {e}")
    
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

if __name__ == "__main__":
    crear_base_datos_y_tabla()
