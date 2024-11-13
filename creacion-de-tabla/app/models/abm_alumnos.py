# app/models/abm_alumnos.py

from app.db_connection import DBConnection

class ABMAlumnos:

    @staticmethod
    def altaAlumno(ci, nombre, apellido, fecha_nacimiento):
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento) VALUES (?, ?, ?, ?)", (ci, nombre, apellido, fecha_nacimiento))
            conexion.commit()
            cursor.close()
            conexion.close()

    @staticmethod
    def bajaAlumno(ci):
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM alumnos WHERE ci = ?", (ci,))
            conexion.commit()
            cursor.close()
            conexion.close()

    @staticmethod
    def modificarAlumno(ci, nuevo_nombre, nuevo_apellido):
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
    def verAlumnoPorCI(ci):
        conexion = DBConnection.conectar_bd()
        alumno = None
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM alumnos WHERE ci = ?", (ci,))
            row = cursor.fetchone()
            if row:
                alumno = {
                    "ci": row[0],
                    "nombre": row[1],
                    "apellido": row[2],
                    "fecha_nacimiento": row[3]
                }
            cursor.close()
            conexion.close()
        return alumno

    @staticmethod
    def verAlumnos():
        conexion = DBConnection.conectar_bd()
        alumnos = []
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM alumnos")
            alumnos = [dict(ci=row[0], nombre=row[1], apellido=row[2], fecha_nacimiento=row[3]) for row in cursor.fetchall()]
            cursor.close()
            conexion.close()
        return alumnos

    

