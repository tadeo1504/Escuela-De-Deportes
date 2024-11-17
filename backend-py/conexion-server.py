import pyodbc
#hay q hacer pip install pyodbc

# Configura tu conexión
server = 'LAPTOP-OMEVDG9L'
database = 'OBLIGATORIO'     
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    # Establecer la conexión
    connection = pyodbc.connect(connection_string)
    print("Conexión exitosa a la base de datos.")

    # # Realiza una consulta de prueba
    # cursor = connection.cursor()
    # cursor.execute("SELECT TOP 5 * FROM alumnos;")  

    # # Imprime los resultados
    # for row in cursor.fetchall():
    #     print(row)

    # Cierra la conexión
    # cursor.close()
    connection.close()
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

