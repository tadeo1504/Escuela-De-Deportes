# Obligatorio/abm_turnos.py
from app.db_connection import DBConnection

class ABMTurnos:
    @staticmethod
    def altaTurnos(id, hora_inicio, hora_final):
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM turnos WHERE id = ?", (id,))
            if cursor.fetchone()[0] > 0:
                raise Exception("No se puede registrar el turno porque ya existe un horario para ese ID.")
            
            cursor.execute("INSERT INTO turnos (id, hora_inicio, hora_final) VALUES (?, ?, ?)", 
                           (id, hora_inicio, hora_final))
            conexion.commit()
        except Exception as e:
            raise Exception(f"Error al registrar el turno: {e}")
        finally:
            cursor.close()
            conexion.close()
    
    @staticmethod
    def verTurnos():
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM turnos")
            return [{"id": row[0], "hora_inicio": str(row[1])[:5], "hora_final": str(row[2])[:5]} for row in cursor.fetchall()]
        except Exception as e:
            raise Exception(f"Error al mostrar todos los turnos: {e}")
        finally:
            cursor.close()
            conexion.close()

