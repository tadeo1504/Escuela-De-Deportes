from app.db_connection import DBConnection

class Equipamiento:
    @staticmethod
    def verEquipamiento():
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM equipamiento")
            columnas = [column[0] for column in cursor.description]  # Obtener nombres de las columnas
            resultados = cursor.fetchall()
            equipamiento = [dict(zip(columnas, fila)) for fila in resultados]  # Convertir cada fila a diccionario
            return equipamiento
        except Exception as e:
            raise Exception(f"Error al mostrar el equipamiento: {e}")
        finally:
            cursor.close()
            conexion.close()

            
    def altaEquipamiento(nombre, cantidad):
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO equipamiento (nombre, cantidad) VALUES (?, ?)", (nombre, cantidad))
            conexion.commit()
        except Exception as e:
            raise Exception(f"Error al registrar el equipamiento: {e}")
        finally:
            cursor.close()
            conexion.close()
    
    def bajaEquipamiento(id):
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM equipamiento WHERE id = ?", (id,))
            conexion.commit()
        except Exception as e:
            raise Exception(f"Error al eliminar el equipamiento: {e}")
        finally:
            cursor.close()
            conexion.close()
            
    def modificarEquipamiento(id, nombre, cantidad):
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("UPDATE equipamiento SET nombre = ?, cantidad = ? WHERE id = ?", (nombre, cantidad, id))
            conexion.commit()
        except Exception as e:
            raise Exception(f"Error al modificar el equipamiento: {e}")
        finally:
            cursor.close()
            conexion.close()
            
    
