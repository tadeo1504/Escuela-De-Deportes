# main.py
from abm_instructores import ABMInstructores
from abm_alumnos import ABMAlumnos
from abm_turnos import ABMTurnos
from gestion_clases import GestionClases
from modificaciones_actividades import ModificacionesActividades

def menu():
    while True:
        print("\n--- Menú ---\n--- Deportes de Nieve ---")
        print("1. ABM de Instructores")
        print("2. ABM de Turnos")
        print("3. ABM de Alumnos")
        print("4. Modificación de Actividades")
        print("5. Gestión de Clases")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            ABMInstructores.altaInstructor() # Usar métodos de ABMInstructores
        elif opcion == 2:
            ABMTurnos.altaTurnos()  # Usar métodos de ABMTurnos
        elif opcion == 3:
            ABMAlumnos.altaAlumno()  # Usar métodos de ABMAlumnos
        elif opcion == 4:
            ModificacionesActividades.modificarDeportes()  # Usar métodos de ModificacionesActividades
        elif opcion == 5:
            GestionClases.asignarInstructores()  # Usar métodos de GestionClases
        elif opcion == 6:
            print("Salir")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == '__main__':
    menu()
