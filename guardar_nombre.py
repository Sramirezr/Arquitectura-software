import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin123',  # Cambia si tu root tiene contraseña
    database='usuario'
)

cursor = conexion.cursor()

# Pedir nombre
nombre = input("Ingresa tu nombre: ")

# Insertar en la tabla
sql = "INSERT INTO nombres (nombre) VALUES (%s)"
cursor.execute(sql, (nombre,))

# Confirmar y cerrar
conexion.commit()
print("Nombre guardado correctamente.")

cursor.close()
conexion.close()
