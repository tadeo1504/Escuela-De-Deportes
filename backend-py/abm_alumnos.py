# Obligatorio/abm_alumnos.py
from escuela_deportes_nieve import EscuelaDeportesNieve

class ABMAlumnos:

    @staticmethod
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

    @staticmethod
    def bajaAlumno():
        print("Ingrese CI del alumno a dar de baja:")
        ci = input()
        print("Alumno dado de baja con éxito.")

    @staticmethod
    def modificarAlumno():
        print("Ingrese CI del alumno a modificar:")
        ci = input()
        print("Ingrese nuevo nombre (dejar vacío si no desea cambiar):")
        nuevo_nombre = input()
        print("Ingrese nuevo apellido (dejar vacío si no desea cambiar):")
        nuevo_apellido = input()
        print("Datos del alumno actualizados con éxito.")

    @staticmethod
    def verAlumnos():
        conexion = EscuelaDeportesNieve.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM alumnos")
            for row in cursor.fetchall():
                print(row)
            cursor.close()
            conexion.close()
