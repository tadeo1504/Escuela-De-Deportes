# Obligatorio/gestion_clases.py

class GestionClases:

    @staticmethod
    def asignarInstructores():
        print("Ingrese el deporte:")
        deporte = input()
        print("Ingrese el instructor:")
        instructor = input()
        print("Instructor asignado con éxito.")

    @staticmethod
    def asignarAlumnos():
        print("Ingrese el deporte:")
        deporte = input()
        print("Ingrese el alumno:")
        alumno = input()
        print("Alumno asignado con éxito.")

    @staticmethod
    def verActividades():
        conexion = EscuelaDeportesNieve.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM actividades")
            for row in cursor.fetchall():
                print(row)
            cursor.close()
            conexion.close()
