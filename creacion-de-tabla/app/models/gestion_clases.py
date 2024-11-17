# Obligatorio/gestion_clases.py
from app.db_connection import DBConnection

class GestionClases:

    @staticmethod
    def crearClase(ci_instructor, id_actividad, id_turno, dictada):
        """
        Crea una nueva clase en la base de datos con los valores proporcionados.

        :param ci_instructor: CI del instructor.
        :param id_actividad: ID de la actividad.
        :param id_turno: ID del turno.
        :param dictada: Estado de la clase ("si" para activa, "no" para inactiva).
        """
        print("Para crear la clase, asegúrese de que el instructor, la actividad y el turno estén registrados.")

        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute(
                    "INSERT INTO clase ( ci_instructor, id_actividad, id_turno, dictada) VALUES (?, ?, ?, ?)",
                    ( ci_instructor, id_actividad, id_turno, dictada)
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
        clases = []  # Lista para almacenar los resultados en formato de diccionario
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
                        
                        clase = {
                            "nombre_instructor": row[0],
                            "apellido_instructor": row[1],
                            "descripcion_actividad": row[2],
                            "hora_inicio": str(row[3])[:5],
                            "hora_final": str(row[4])[:5],
                            "dictada": row[5],
                            "id_clase": row[6]
                        }
                        clases.append(clase)  
                else:
                    print("No se encontraron clases.")
            except Exception as e:
                print("Error al mostrar todas las clases:", e)
            finally:
                cursor.close()
                conexion.close()
        return clases  
