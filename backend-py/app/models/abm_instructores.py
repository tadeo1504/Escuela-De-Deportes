# app/models/abm_instructores.py

from app.db_connection import DBConnection

class ABMInstructores:

    @staticmethod
    def altaInstructor(ci, nombre, apellido):
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO instructores (ci, nombre, apellido) VALUES (?, ?, ?)", (ci, nombre, apellido))
            conexion.commit()
            cursor.close()
            conexion.close()

    @staticmethod
    def bajaInstructor(ci):
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            
            cursor.execute("SELECT * FROM clase WHERE ci_instructor = ?", (ci,))
            asignacion = cursor.fetchone()
            
            if asignacion:
                cursor.close()
                conexion.close()
                raise Exception("Este instructor está asignado a un curso y no puede ser eliminado.")
            
            cursor.execute("DELETE FROM instructores WHERE ci = ?", (ci,))
            conexion.commit()
            cursor.close()
            conexion.close()

    @staticmethod
    def modificarInstructor(ci, nuevo_nombre, nuevo_apellido):
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            if nuevo_nombre:
                cursor.execute("UPDATE instructores SET nombre = ? WHERE ci = ?", (nuevo_nombre, ci))
            if nuevo_apellido:
                cursor.execute("UPDATE instructores SET apellido = ? WHERE ci = ?", (nuevo_apellido, ci))
            conexion.commit()
            cursor.close()
            conexion.close()
   

    @staticmethod
    def verInstructores():
        conexion = DBConnection.conectar_bd()
        instructores = []
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM instructores")
            instructores = [dict(ci=row[0], nombre=row[1], apellido=row[2]) for row in cursor.fetchall()]
            cursor.close()
            conexion.close()
        return instructores

    


    @staticmethod
    def verInstructorPorCI(ci):
        conexion = DBConnection.conectar_bd()
        instructor = None
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM instructores WHERE ci = ?", (ci,))
            row = cursor.fetchone()
            if row:
                instructor = {
                    "ci": row[0],
                    "nombre": row[1],
                    "apellido": row[2],
                }
            cursor.close()
            conexion.close()
        print(instructor)
        return instructor