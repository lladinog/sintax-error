import mysql.connector

try:
    cnx = mysql.connector.connect(
        host="localhost", # O 127.0.0.1
        user="root",
        password="@CP2006-Maths",
        database="db_nilo"
    )
    print("Conexión exitosa a la base de datos.")
    cnx.close()
except mysql.connector.Error as err:
    print(f"Error al conectar: {err}")