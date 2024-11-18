# Obligatorio/abm_turnos.py
from app.db_connection import DBConnection

class ABMTurnos:
    @staticmethod
    def altaTurnos( hora_inicio, hora_final):
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO turnos (hora_inicio, hora_final) VALUES (?, ?)", 
                           (hora_inicio, hora_final))
            conexion.commit()
        except Exception as e:
            raise Exception(f"Error al registrar el turno: {e}")
        finally:
            cursor.close()
            conexion.close()
    
    @staticmethod
    def verTurnos():
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("SELECT * FROM turnos")
                return [{"id": row[0], "hora_inicio": str(row[1])[:5], "hora_final": str(row[2])[:5]} for row in cursor.fetchall()]
            except Exception as e:
                raise Exception(f"Error al mostrar todos los turnos: {e}")
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def modificarTurnos(id, hora_inicio, hora_final):
        """
        Modifica un turno existente en la base de datos.
        
        :param id: ID del turno a modificar.
        :param hora_inicio: Nueva hora de inicio.
        :param hora_final: Nueva hora de finalización.
        """
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("SELECT COUNT(*) FROM turnos WHERE id = ?", (id,))
                if cursor.fetchone()[0] == 0:
                    raise Exception("El turno no existe y no se puede modificar.")
                
                cursor.execute(
                    "UPDATE turnos SET hora_inicio = ?, hora_final = ? WHERE id = ?",
                    (hora_inicio, hora_final, id)
                )
                conexion.commit()
            except Exception as e:
                raise Exception(f"Error al modificar el turno: {e}")
            finally:
                cursor.close()
                conexion.close()
                
    @staticmethod
    def bajaTurnos(id):
        """
        Elimina un turno por su ID.
        
        :param id: ID del turno a eliminar.
        """
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("SELECT COUNT(*) FROM turnos WHERE id = ?", (id,))
                if cursor.fetchone()[0] == 0:
                    raise Exception("El turno no existe y no se puede eliminar.")
                
                cursor.execute("DELETE FROM turnos WHERE id = ?", (id,))
                conexion.commit()
            except Exception as e:
                raise Exception(f"Error al eliminar el turno: {e}")
            finally:
                cursor.close()
                conexion.close()

    