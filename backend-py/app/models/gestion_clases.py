# Obligatorio/gestion_clases.py
from app.db_connection import DBConnection

class GestionClases:

    @staticmethod
    def crearClase():
        print("Para crear la clase ya debe tener registrado al instructor a cargo, actividad a realizar, el turno, y saber si va a ser clase activa")
        print("Ingrese la CI del Instructor:")
        ci_instructor = input()
        print("Ingrese el id de la Actividad:")
        id_actividad = input()
        print("Ingrese el id del turno que se va a realizar")
        id_turno = input()
        print("Ingrese si para dar como activa o no para colocarla como inactiva a la clase")
        dictada = input()
        print("Instructor asignado con éxito.")
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute(
                    "INSERT INTO clase (ci_instructor, id_actividad, id_turno, dictada) VALUES (?, ?, ?, ?)",
                    (ci_instructor, id_actividad, id_turno, dictada)
                )
                conexion.commit()
                print("Clase creada con éxito.")
            except Exception as e:
                print(f"Ocurrió un error al crear la clase: {e}")
            finally:
                cursor.close()
                conexion.close()
            
    @staticmethod
    def eliminarClase():
        print("Ingrese el ID de la clase que desea eliminar:")
        id_clase = input()
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("DELETE FROM clase WHERE id = ?", (id_clase))
                clase = cursor.fetchone()
                conexion.commit()
                print("Clase eliminada con éxito.")
            except Exception as e:
                print(f"Ocurrió un error al eliminar la clase: {e}")
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def verClases():
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            try: 
                cursor.execute(
                "SELECT instructores.nombre, instructores.apellido, actividades.descripcion, "
                "turnos.hora_inicio, turnos.hora_final, clase.dictada, clase.id "
                "FROM clase "
                "JOIN instructores ON clase.ci_instructor = instructores.ci "
                "JOIN actividades ON clase.id_actividad = actividades.id "
                "JOIN turnos ON clase.id_turno = turnos.id"
                )
                resultados = cursor.fetchall()  
                if resultados:
                    for row in resultados: 
                        print(row)  
                else:
                    print("No se encontraron clases.")
            except Exception as e:
                print("Error al mostrar todas las clases")
            finally:
                cursor.close()
                conexion.close()