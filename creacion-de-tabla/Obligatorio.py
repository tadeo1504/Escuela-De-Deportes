import pyodbc


class EscuelaDeportesNieve:

    def submenuReportes():
        print("1 Reporte de Instructores")
        print("2 Reporte de Turnos")
        print("3 Reporte de Alumnos")
        print("4 Reporte de Actividades")
        while opcion != 5:
            if opcion == '1':
                        """"""
            elif opcion == '2':
                """"""
            elif opcion == '3':
                """"""
            elif opcion == '4':
                """"""
            elif opcion == '5':
                print("Salir")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def submenuModificaciones():
        print("1 Modificación de Deportes")
        print("2 Modificación de Horarios")
        while opcion != 3:
            if opcion == '1':
                """"""
            elif opcion == '2':
                """"""
            elif opcion == '3':
                print("Salir")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

def altaInstructor():
    print("Ingrese CI:")
    ci = input()  
    print("Ingrese el nombre:")
    nombre = input()  
    print("Ingrese el apellido:")
    apellido = input()  
    print("Instructor registrado con éxito.")
     
    # Conectar a la base de datos
    conexion = conectar_bd()
    cursor = conexion.cursor()

    # Ejecutar el INSERT
    try:
        cursor.execute("""
            INSERT INTO instructores (ci, nombre, apellido)
            VALUES (?, ?, ?)
        """, (ci, nombre, apellido))
        conexion.commit()  # Confirmar los cambios
        print("Instructor registrado con éxito.")
    except Exception as e:
        print("Error al registrar el instructor:", e)
    finally:
        cursor.close()
        conexion.close()


def bajaInstructor():
    print("Ingrese CI del instructor a dar de baja:")
    ci = input()
    print("Instructor dado de baja con éxito.")
     # Conectar a la base de datos
    conexion = conectar_bd()
    cursor = conexion.cursor()

    # Ejecutar el DELETE
    try:
        cursor.execute("""
            DELETE FROM instructores
            WHERE ci = ?
        """, (ci,))
        conexion.commit()  # Confirmar los cambios
        if cursor.rowcount > 0:
            print("Instructor dado de baja con éxito.")
        else:
            print("No se encontró ningún instructor con ese CI.")
    except Exception as e:
        print("Error al dar de baja el instructor:", e)
    finally:
        cursor.close()
        conexion.close()

def modificarInstructor():
    print("Ingrese CI del instructor a modificar:")
    ci = input() 
    print("Ingrese nuevo nombre (dejar vacío si no desea cambiar):")
    nuevo_nombre = input()  
    print("Ingrese nuevo apellido (dejar vacío si no desea cambiar):")
    nuevo_apellido = input()
    print("Datos del instructor actualizados con éxito.")
    # ACA PUEDE MODIFICAR TODO O NADA
    

    def submenuABMinstructores():
        print("\n--- ABM de Instructores ---")
        print("1 Alta de Instructores")
        print("2 Baja de Instructores")
        print("3 Modificaciones de Instructores")
        while opcion != 4:
            if opcion == '1':
                altaInstructor()
            elif opcion == '2':
                bajaInstructor()
            elif opcion == '3':
                modificarInstructor()
            elif opcion == '4':
                print("Salir")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

def altaAlumno():
    print("Ingrese CI:")
    ci = input()  
    print("Ingrese el nombre:")
    nombre = input()  
    print("Ingrese el apellido:")
    apellido = input()  
    print("Ingrese fecha de nacimiento (DD/MM/AAAA):")
    fecha_nacimiento = input() 
    print("Ingrese teléfono de contacto:")
    telefono = input()  
    print("Ingrese el correo electrónico:")
    correo = input() 
    print("Alumno registrado con éxito.")

def bajaAlumno():
    print("Ingrese CI del alumno a dar de baja:")
    ci = input()  
    print("Alumno dado de baja con éxito.")

def modificarAlumno():
    print("Ingrese CI del alumno a modificar:")
    ci = input()  
    nuevo_nombre = input()  
    print("Ingrese nuevo apellido (dejar vacío si no desea cambiar):")
    nuevo_apellido = input()  
    print("Datos del alumno actualizados con éxito.")

    def submenuABMalumnos():
        while True:
            print("\n--- ABM de Alumnos ---")
            print("1. Alta de alumnos")
            print("2. Baja de alumnos")
            print("3. Modificaciones de alumnos")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                altaAlumno()
            elif opcion == '2':
                bajaAlumno()
            elif opcion == '3':
                modificarAlumno()
            elif opcion == '4':
                print("Salir")
                break
            else:
                print("Opción no válida. Intente nuevamente.")


    def submenuABMturnos():
        print("\n--- ABM de Turnos ---")
        print("1 Alta de turnos")
        print("2 Baja de turnos")
        print("3 Modificaciones de turnos")
        while opcion != 5:
            if opcion == '1':
                        """"""
            elif opcion == '2':
                """"""
            elif opcion == '3':
                """"""
            elif opcion == '4':
                print("Salir")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        
    def costosDeportes():
        """"""
    
    def restriccionesDeportes():
        """"""

    def verDeportes():
        query = "SELECT * FROM actividades;"
        cursor.execute(query)

    def menu():
            while True:
                print("\n--- Menú ---\n--- Deportes de Nieve ---")
                print("1. ABM de Instructores")    #Alta, baja y modificación (ABM)
                print("2. ABM de Turnos")
                print("3. ABM de Alumnos")
                print("4. Modificación de Actividades")
                print("5. Gestión de Clases")
                print("6. Reportes")
                print("7. Salir")
                opcion = input("Seleccione una opción: ")

                if opcion == '1':
                    """"""
                elif opcion == '2':
                    """"""
                elif opcion == '3':
                    """"""
                elif opcion == '4':
                    """"""
                elif opcion == '5':
                    """"""
                elif opcion == '6':
                    """"""
                elif opcion == '7':
                    print("Salir")
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")

    def Saludo():
        print("Hello juanita")

    try:
        # Configura la conexión con autenticación de Windows de SQL Server
        conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=DESKTOP-8L3U16R;'
                'DATABASE=ObligatorioBD;'
                'Trusted_Connection=yes;'
            )
        cursor = conn.cursor()

            # Ejecutar una consulta de ejemplo
        query = "SELECT * FROM actividades;"
        cursor.execute(query)

            # Mostrar los resultados
        for row in cursor:
            print(row)

        conn.close()
        menu()
        Saludo()
        
    except pyodbc.Error as e:
        print("Error al conectar con la base de datos:", e)


