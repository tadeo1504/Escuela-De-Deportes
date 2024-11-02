# Obligatorio/abm_turnos.py
from db_connection import DBConnection

class ABMTurnos:

    @staticmethod
    def altaTurnos():
        id = 0
        print("Ingrese la hora de inicio (HH:MM):")
        hora_inicio = input()  
        print("Ingrese la hora final (HH:MM):")
        hora_final = input()   
        print("Ingrese el turno del 1 al 4")
        id = input()
        print("")
        conexion = DBConnection.conectar_bd()
        try:
            conexion = DBConnection.conectar_bd()
            if conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT COUNT(*) FROM turnos WHERE id = ?", (id,))
                existe = cursor.fetchone()[0]
                if existe > 0:
                    print("No se puede registrar el turno porque ya existe un horario para ese ID.")
                else:
                    cursor.execute("INSERT INTO turnos (id, hora_inicio, hora_final) VALUES (?, ?, ?)", (id, hora_inicio, hora_final))
                    conexion.commit()
                    print("Turno registrado con éxito.")
        except Exception as e:
            print(f"Ocurrió un error al registrar el turno: {e}")
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def bajaTurnos():
        print("Ingrese el id del turno a dar de baja:")
        idbaja = input()
        print("Turno dado de baja con éxito.")
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM turnos WHERE id = ?", (idbaja))
            conexion.commit()
            cursor.close()
            conexion.close()

    @staticmethod
    def modificarTurnos():
        print("Ingrese el id del turno a modificar:")
        id = input()
        print("Ingrese el nuevo horario de inicio (dejar vacío si no desea cambiar):")
        hora_inicio = input()
        print("Ingrese el nuevo horario final (dejar vacío si no desea cambiar):")
        hora_final = input()
        print("Datos del turno actualizados con éxito.")
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            if hora_inicio:
                cursor.execute("UPDATE turnos SET hora_inicio = ? WHERE id = ?", (hora_inicio, id))
            if hora_final:
                cursor.execute("UPDATE turnos SET hora_final = ? WHERE id = ?", (hora_final, id))
            conexion.commit()
            cursor.close()
            conexion.close()

    @staticmethod
    def verTurnos():
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM turnos")
            for row in cursor.fetchall():
                print(row)
            cursor.close()
            conexion.close()
