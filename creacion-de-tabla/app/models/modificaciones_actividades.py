from app.db_connection import DBConnection

class ModificacionesActividades:
    @staticmethod
    def agregarDeportes(id, nombre, costo):
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO actividades VALUES (?, ?, ?)", (id, nombre, costo))
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
            cursor.execute("DELETE FROM actividades WHERE id = ?", (id,))
            conexion.commit()
        except Exception as e:
            raise Exception(f"Error al eliminar el deporte: {e}")
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
            return [{"id": row[0], "nombre": row[1], "costo": row[2]} for row in resultados]
        except Exception as e:
            raise Exception(f"Error al mostrar todas las actividades: {e}")
        finally:
            cursor.close()
            conexion.close()
