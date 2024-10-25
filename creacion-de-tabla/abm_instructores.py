# Obligatorio/abm_instructores.py
from escuela_deportes_nieve import EscuelaDeportesNieve

class ABMInstructores:

    @staticmethod
    def altaInstructor():
        print("Ingrese CI:")
        ci = input()
        print("Ingrese el nombre:")
        nombre = input()
        print("Ingrese el apellido:")
        apellido = input()
        
        conexion = EscuelaDeportesNieve.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO instructores (ci, nombre, apellido) VALUES (?, ?, ?)", (ci, nombre, apellido))
            conexion.commit()
            print("Instructor registrado con éxito.")
        except Exception as e:
            print("Error al registrar el instructor:", e)
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def bajaInstructor():
        print("Ingrese CI del instructor a dar de baja:")
        ci = input()
        
        conexion = EscuelaDeportesNieve.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM instructores WHERE ci = ?", (ci,))
            conexion.commit()
            if cursor.rowcount > 0:
                print("Instructor dado de baja con éxito.")
            else:
                print("No se encontró ningún instructor con ese CI.")
        except Exception as e:
            print("Error al dar de baja el instructor:", e)
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def modificarInstructor():
        print("Ingrese CI del instructor a modificar:")
        ci = input()
        print("Ingrese nuevo nombre (dejar vacío si no desea cambiar):")
        nuevo_nombre = input()
        print("Ingrese nuevo apellido (dejar vacío si no desea cambiar):")
        nuevo_apellido = input()
        print("Datos del instructor actualizados con éxito.")

    @staticmethod
    def verInstructores():
        conexion = EscuelaDeportesNieve.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM instructores")
            for row in cursor.fetchall():
                print(row)
            cursor.close()
            conexion.close()
