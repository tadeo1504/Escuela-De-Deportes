# main.py
from escuela_deportes_nieve import EscuelaDeportesNieve
from db_connection import DBConnection

def menu():
    while True:
        print("\n--- Menú ---\n--- Deportes de Nieve ---")
        print("1. ABM de Instructores")
        print("2. ABM de Turnos")
        print("3. ABM de Alumnos")
        print("4. Modificación de Actividades")
        print("5. Gestión de Clases")
        print("6. Reportes")
        print("7. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            EscuelaDeportesNieve.submenuABMinstructores()
        elif opcion == 2:
            EscuelaDeportesNieve.submenuABMturnos()
        elif opcion == 3:
            EscuelaDeportesNieve.submenuABMalumnos()
        elif opcion == 4:
            EscuelaDeportesNieve.submenuModificacionesActividades()
        elif opcion == 5:
            EscuelaDeportesNieve.submenuGestionClases()
        elif opcion == 6:
            EscuelaDeportesNieve.submenuReportes()
        elif opcion == 7:
            print("Salir")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
