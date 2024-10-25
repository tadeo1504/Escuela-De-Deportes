import pyodbc

class EscuelaDeportesNieve:

    #Guillermo 
    @staticmethod
    def conectar_bd():
        try:
            conexion = pyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=LAPTOP-K7AU665T;'  
                'DATABASE=Obligatorio;'      
                'Trusted_Connection=yes;' 
            )
            return conexion
        except pyodbc.Error as e:
            print("Error al conectar con la base de datos:", e)
            return None


def submenuReportes(): #FALTA BUSCAR UN GENERADOR DE PDF PARA SACAR LOS REPORTES CREO O SINO SERIA IMPRIMIR ALGO FACIL EN CONSOLA LOS RESULTADOS
    while True:
        print("1 Reporte de Instructores")
        print("2 Reporte de Turnos")
        print("3 Reporte de Alumnos")
        print("4 Reporte de Actividades")
        print("5 Salir")
        opcion = int(input("Seleccione una opción: "))  
        if opcion == 1:
            """"""
        elif opcion == 2:
            """"""
        elif opcion == 3:
            """"""
        elif opcion == 4:
            """"""
        elif opcion == 5:
            print("Salir")
            break
        else:
            print("Opción no válida. Intente nuevamente.")





def submenuABMinstructores():
    while True:
        print("\n--- ABM de Instructores ---")
        print("1 Alta de Instructores")
        print("2 Baja de Instructores")
        print("3 Modificaciones de Instructores")
        print("4 Ver Instructores")
        print("5 Salir")
        opcion = int(input("Seleccione una opción: "))  
        if opcion == 1:
            altaInstructor()
        elif opcion == 2:
            bajaInstructor()
        elif opcion == 3:
            modificarInstructor()
        elif opcion == 4:
            verInstructores()
        elif opcion == 5:
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

def verAlumnos():
    conexion = EscuelaDeportesNieve.conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        query = "SELECT * FROM alumnos;"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        conexion.close()

def submenuABMalumnos():
    while True:
        print("\n--- ABM de Alumnos ---")
        print("1. Alta de alumnos")
        print("2. Baja de alumnos")
        print("3. Modificaciones de alumnos")
        print("4. Ver alumnos")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            altaAlumno()
        elif opcion == 2:
            bajaAlumno()
        elif opcion == 3:
            modificarAlumno()
        elif opcion == 4:
            verAlumnos()
        elif opcion == 5:
            print("Salir")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def asignarInstructores():
    print("Ingrese el deporte:")
    deporte = input()
    print("Ingrese el instructor:")
    instructor = input()
    print("Instructor asignado con éxito.")

def asignarAlumnos():
    print("Ingrese el deporte:")
    deporte = input()
    print("Ingrese el alumno:")
    alumno = input()
    print("Alumno asignado con éxito.")

def verActividades():
    conexion = EscuelaDeportesNieve.conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        query = "SELECT * FROM actividades;"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        conexion.close()
        menu()

def submenuGestionClases():
    while True:
        print("1 Asignar instructores a actividades")
        print("2 Asignar alumnos a actividades")
        print("3 Ver actividades")
        print("4 Salir")
        opcion = int(input("Seleccione una opción: "))  
        if opcion == 1:
            asignarInstructores()
        elif opcion == 2:
            asignarAlumnos()
        elif opcion == 3:
            verActividades()
        elif opcion == 4:
            print("Salir")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def modificacionHorarios():
    print("Ingrese el horario a modificar: ")
    horario = input()
    print("Ingrese el nuevo horario: ")
    nuevo_horario = input()
    print("Horario modificado con éxito.")  

def modificarDeportes():
    print("Ingrese el deporte a modificar: ")
    deporte = input()
    print("Ingrese el nuevo deporte: ")
    nuevo_deporte = input()
    print("Deporte modificado con éxito.")
    
def submenuModificacionesActividades():
    while True:
        print("1 Modificación de Deportes")
        print("2 Modificación de Horarios")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            modificarDeportes()
        elif opcion == 2:
            modificacionHorarios()
        elif opcion == 3:
            print("Salir")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def altaTurnos():
    print("Ingrese el horario:")
    horario = input()
    print("Ingrese la fecha (DD/MM/AAAA):")
    fecha = input()
    print("Turno registrado con éxito.")

def bajaTurnos():
    print("Ingrese el horario del turno a dar de baja:")
    horario = input()
    print("Ingrese la fecha del turno a dar de baja:")
    fecha = input()
    print("Turno dado de baja con éxito.")

def modificarTurnos():
    print("Ingrese el horario del turno a modificar:")
    horario = input()
    print("Ingrese la fecha del turno a modificar:")
    fecha = input()
    print("Ingrese el nuevo horario (dejar vacío si no desea cambiar):")
    nuevo_horario = input()
    print("Ingrese la nueva fecha (dejar vacío si no desea cambiar):")
    nueva_fecha = input()
    print("Datos del turno actualizados con éxito.")

def verTurnos():
    conexion = EscuelaDeportesNieve.conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        query = "SELECT * FROM turnos;"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        conexion.close()


def submenuABMturnos():
    while True:
        print("\n--- ABM de Turnos ---")
        print("1 Alta de turnos")
        print("2 Baja de turnos")
        print("3 Modificaciones de turnos")
        print("4 Ver todos los Turnos")
        print("5 Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            altaTurnos()
        elif opcion == 2:
            bajaTurnos()
        elif opcion == 3:
            modificarTurnos()
        elif opcion == 4:
            verTurnos()
        elif opcion == 5:
            print("Salir")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu():
    while True:
        print("\n--- Menú ---\n--- Deportes de Nieve ---")
        print("1. ABM de Instructores")
        print("2. ABM de Turnos")
        print("3. ABM de Alumnos")
        print("4. Modificación de Actividades")
        print("5. Gestión de Clases")
        print("6. Reportes")
        print("7. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            submenuABMinstructores()
        elif opcion == 2:
            submenuABMturnos()
        elif opcion == 3:
            submenuABMalumnos()
        elif opcion == 4:
            submenuModificacionesActividades()
        elif opcion == 5:
            submenuGestionClases()
        elif opcion == 6:
            submenuReportes()
        elif opcion == 7:
            print("Salir")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def Saludo():
    print("Hello juanita")

if __name__ == '__main__':
    menu()

        
    
