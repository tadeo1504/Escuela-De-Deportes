import pyodbc

from db_connection import DBConnection
from abm_instructores import ABMInstructores
from abm_turnos import ABMTurnos
from abm_alumnos import ABMAlumnos
from modificaciones_actividades import ModificacionesActividades
from gestion_clases import GestionClases


class EscuelaDeportesNieve:

    def submenuReportes(): #FALTA BUSCAR UN GENERADOR DE PDF PARA SACAR LOS REPORTES CREO O SINO SERIA IMPRIMIR ALGO FACIL EN CONSOLA LOS RESULTADOS
        while True:
            print("1 Reporte de Instructores")
            print("2 Reporte de Turnos")
            print("3 Reporte de Alumnos")
            print("4 Reporte de Actividades")
            print("5 Salir")
            opcion = int(input("Seleccione una opción: "))  
            if opcion == 1:
                """"""
            elif opcion == 2:
                """"""
            elif opcion == 3:
                """"""
            elif opcion == 4:
                """"""
            elif opcion == 5:
                print("Salir")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def submenuABMinstructores():
        while True:
            print("\n--- ABM de Instructores ---")
            print("1 Alta de Instructores")
            print("2 Baja de Instructores")
            print("3 Modificaciones de Instructores")
            print("4 Ver Instructores")
            print("5 Salir")
            opcion = int(input("Seleccione una opción: "))  
            if opcion == 1:
                ABMInstructores.altaInstructor()
            elif opcion == 2:
                ABMInstructores.bajaInstructor()
            elif opcion == 3:
                ABMInstructores.modificarInstructor()
            elif opcion == 4:
                ABMInstructores.verInstructores()
            elif opcion == 5:
                print("Salir")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def submenuABMalumnos():
        while True:
            print("\n--- ABM de Alumnos ---")
            print("1. Alta de alumnos")
            print("2. Baja de alumnos")
            print("3. Modificaciones de alumnos")
            print("4. Ver alumnos")
            print("5. Salir")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                ABMAlumnos.altaAlumno()
            elif opcion == 2:
                ABMAlumnos.bajaAlumno()
            elif opcion == 3:
                ABMAlumnos.modificarAlumno()
            elif opcion == 4:
                ABMAlumnos.verAlumnos()
            elif opcion == 5:
                print("Salir")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def submenuGestionClases():
        while True:
            print("1 Crear Clase")
            print("2 Eliminar Clase")
            print("3 Ver todas las clases")
            print("4 Salir")
            opcion = int(input("Seleccione una opción: "))  
            if opcion == 1:
                GestionClases.crearClase()
            elif opcion == 2:
                GestionClases.eliminarClase()
            elif opcion == 3:
                GestionClases.verClases()
            elif opcion == 4:
                print("Salir")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        
    def submenuModificacionesActividades():
        while True:
            print("1 Ver todos los Deportes")
            print("2 Agregar Deportes")
            print("3 Eliminar Deportes")
            print("4 Salir")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                ModificacionesActividades.verDeportes()
            elif opcion == 2:
                ModificacionesActividades.agregarDeportes()
            elif opcion == 3:
                ModificacionesActividades.eliminarDeportes()
            elif opcion == 4:
                print("Salir")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def submenuABMturnos():
        while True:
            print("\n--- ABM de Turnos ---")
            print("1 Alta de turnos")
            print("2 Baja de turnos")
            print("3 Modificaciones de turnos")
            print("4 Ver todos los Turnos")
            print("5 Salir")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                ABMTurnos.altaTurnos()
            elif opcion == 2:
                ABMTurnos.bajaTurnos()
            elif opcion == 3:
                ABMTurnos.modificarTurnos()
            elif opcion == 4:
                ABMTurnos.verTurnos()
            elif opcion == 5:
                print("Salir")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

