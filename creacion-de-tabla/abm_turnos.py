# Obligatorio/abm_turnos.py
from escuela_deportes_nieve import EscuelaDeportesNieve

class ABMTurnos:

    @staticmethod
    def altaTurnos():
        print("Ingrese el horario:")
        horario = input()
        print("Ingrese la fecha (DD/MM/AAAA):")
        fecha = input()
        print("Turno registrado con éxito.")

    @staticmethod
    def bajaTurnos():
        print("Ingrese el horario del turno a dar de baja:")
        horario = input()
        print("Ingrese la fecha del turno a dar de baja:")
        fecha = input()
        print("Turno dado de baja con éxito.")

    @staticmethod
    def modificarTurnos():
        print("Ingrese el horario del turno a modificar:")
        horario = input()
        print("Ingrese la fecha del turno a modificar:")
        fecha = input()
        print("Ingrese el nuevo horario (dejar vacío si no desea cambiar):")
        nuevo_horario = input()
        print("Ingrese la nueva fecha (dejar vacío si no desea cambiar):")
        nueva_fecha = input()
        print("Datos del turno actualizados con éxito.")

    @staticmethod
    def verTurnos():
        conexion = EscuelaDeportesNieve.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM turnos")
            for row in cursor.fetchall():
                print(row)
            cursor.close()
            conexion.close()
