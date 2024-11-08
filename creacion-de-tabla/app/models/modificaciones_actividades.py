# Obligatorio/modificaciones_actividades.py
from app.db_connection import DBConnection


class ModificacionesActividades:

    @staticmethod
    def agregarDeportes():
        print("Ingrese el nuevo Deporte:")
        nuevo_deporte = input()
        print("Ingrese el id del Deporte")
        id = input()
        print("Ingrese el costo que va a tener ")
        costo = input()
        print("Deporte agregado")
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO actividades VALUES (?,?,?)", (id, nuevo_deporte, costo))
            conexion.commit()
        except Exception as e:
            print("Error al agregar el deporte:", e)
        finally:
            cursor.close()
            conexion.close()



    @staticmethod
    def eliminarDeportes():
        print("Ingrese el id para eliminar:")
        ideliminar = input()
        print("El Deporte fue eliminado")
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM actividades WHERE id = (?)", (ideliminar))
            conexion.commit()
        except Exception as e:
            print("Error al eliminar el deporte", e)
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def verDeportes():
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try: 
            cursor.execute("SELECT * FROM actividades")
            resultados = cursor.fetchall()  
            if resultados:
                for actividad in resultados:
                    print(actividad)  
            else:
                print("No se encontraron actividades.")
        except Exception as e:
            print("Error al mostrar todos los Deportes")
        finally:
            cursor.close()
            conexion.close()

