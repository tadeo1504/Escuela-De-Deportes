# Obligatorio/gestion_clases.py
from app.db_connection import DBConnection

class GestionClases:

    @staticmethod
    def crearClase(ci_instructor, id_actividad, id_turno, dictada):
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            try:
                # Verificar si el instructor ya tiene una clase en el mismo turno
                cursor.execute(
                    "SELECT COUNT(*) FROM clase WHERE ci_instructor = ? AND id_turno = ?",
                    (ci_instructor, id_turno)
                )
                resultado = cursor.fetchone()
                if resultado[0] > 0:
                    raise ValueError("El instructor ya tiene una clase asignada en este turno.")

                # Insertar la nueva clase
                cursor.execute(
                    "INSERT INTO clase (ci_instructor, id_actividad, id_turno, dictada) VALUES (?, ?, ?, ?)",
                    (ci_instructor, id_actividad, id_turno, dictada)
                )
                conexion.commit()
                return True
            except ValueError as ve:
                raise ve
            except Exception as e:
                raise Exception(f"Error al crear la clase: {e}")
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

    @staticmethod
    def obtener_clase_por_id(id_clase):
        """Obtiene los datos de una clase específica."""
        conexion = DBConnection.conectar_bd()
        clase = None
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("SELECT ci_instructor, id_actividad, id_turno, dictada FROM clase WHERE id = ?", (id_clase,))
                resultado = cursor.fetchone()
                if resultado:
                    clase = {
                        "ci_instructor": resultado[0],
                        "id_actividad": resultado[1],
                        "id_turno": resultado[2],
                        "dictada": resultado[3],
                    }
            except Exception as e:
                raise Exception(f"Error al obtener la clase: {e}")
            finally:
                cursor.close()
                conexion.close()
        return clase

    

    @staticmethod
    def actualizar_clase(id_clase, nuevos_datos):
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            try:
                # Verificar si el instructor ya tiene una clase en el mismo turno
                cursor.execute(
                    "SELECT COUNT(*) FROM clase WHERE ci_instructor = ? AND id_turno = ? AND id != ?",
                    (
                        nuevos_datos.get("ci_instructor"),
                        nuevos_datos.get("id_turno"),
                        id_clase,
                    )
                )
                resultado = cursor.fetchone()
                if resultado[0] > 0:
                    raise ValueError("El instructor ya tiene una clase asignada en este turno.")

                # Actualizar la clase
                cursor.execute(
                    "UPDATE clase SET ci_instructor = ?, id_actividad = ?, id_turno = ?, dictada = ? WHERE id = ?",
                    (
                        nuevos_datos.get("ci_instructor"),
                        nuevos_datos.get("id_actividad"),
                        nuevos_datos.get("id_turno"),
                        nuevos_datos.get("dictada"),
                        id_clase,
                    )
                )
                conexion.commit()
                if cursor.rowcount == 0:
                    raise Exception("No se encontró la clase para actualizar.")
            except ValueError as ve:
                raise ve
            except Exception as e:
                raise Exception(f"Error al actualizar la clase: {e}")
            finally:
                cursor.close()
                conexion.close()

