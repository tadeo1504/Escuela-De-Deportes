from app.db_connection import DBConnection

class ModificacionesActividades:

    @staticmethod
    def agregarDeportes(nombre, costo):
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO actividades (descripcion, costo) VALUES (?, ?)", (nombre, costo))
            conexion.commit()
        except Exception as e:
            raise Exception(f"Error al agregar el deporte: {e}")
        finally:
            cursor.close()
            conexion.close()
    
    # Agrega id como parámetro en eliminarDeportes
    @staticmethod
    def eliminarDeportes(id):
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            # Eliminar dependencias en la tabla equipamiento
            cursor.execute("DELETE FROM equipamiento WHERE id_actividad = ?", (id,))
            # Luego eliminar el registro en actividades
            cursor.execute("DELETE FROM actividades WHERE id = ?", (id,))
            conexion.commit()
        except Exception as e:
            # Relanzar una excepción personalizada para manejarla en otros niveles
            raise Exception(f"Error al eliminar el deporte: {e}")
        finally:
            # Cerrar siempre la conexión, sea cual sea el resultado
            cursor.close()
            conexion.close()

    
    @staticmethod
    def verDeportes():
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try: 
            cursor.execute("SELECT * FROM actividades")
            resultados = cursor.fetchall()
            return [{"id": row[0], "nombre": row[1], "costo": row[2]} for row in resultados]
        except Exception as e:
            raise Exception(f"Error al mostrar todas las actividades: {e}")
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def modificarDeportes(id, nombre, costo):
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            # Verificar si la actividad existe
            cursor.execute("SELECT COUNT(*) FROM actividades WHERE id = ?", (id,))
            if cursor.fetchone()[0] == 0:
                raise Exception("La actividad no existe y no se puede modificar.")
            
            # Actualizar la actividad
            cursor.execute("UPDATE actividades SET descripcion = ?, costo = ? WHERE id = ?", (nombre, costo, id))
            conexion.commit()
        except Exception as e:
            raise Exception(f"Error al modificar la actividad: {e}")
        finally:
            cursor.close()
            conexion.close()

