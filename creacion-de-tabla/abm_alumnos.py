# Obligatorio/abm_alumnos.py
from db_connection import DBConnection

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
        print("Alumno registrado con éxito.")
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento) VALUES (?, ?, ?, ?)", (ci, nombre, apellido, fecha_nacimiento))
            conexion.commit()
            cursor.close()
            conexion.close()

    @staticmethod
    def bajaAlumno():
        print("Ingrese CI del alumno a dar de baja:")
        ci = input()
        print("Alumno dado de baja con éxito.")
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM alumnos WHERE ci = ?", (ci,))
            conexion.commit()
            cursor.close()
            conexion.close()

    @staticmethod
    def modificarAlumno():
        print("Ingrese CI del alumno a modificar:")
        ci = input()
        print("Ingrese nuevo nombre (dejar vacío si no desea cambiar):")
        nuevo_nombre = input()
        print("Ingrese nuevo apellido (dejar vacío si no desea cambiar):")
        nuevo_apellido = input()
        print("Datos del alumno actualizados con éxito.")
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            if nuevo_nombre:
                cursor.execute("UPDATE alumnos SET nombre = ? WHERE ci = ?", (nuevo_nombre, ci))
            if nuevo_apellido:
                cursor.execute("UPDATE alumnos SET apellido = ? WHERE ci = ?", (nuevo_apellido, ci))
            conexion.commit()
            cursor.close()
            conexion.close()

    @staticmethod
    def verAlumnos():
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM alumnos")
            for row in cursor.fetchall():
                print(row)
            cursor.close()
            conexion.close()
