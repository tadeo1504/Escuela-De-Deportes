# db_connection.py
import pyodbc

class DBConnection:
    @staticmethod
    # def conectar_bd():
    #     try:
    #         #Conexion de Alfonso D.
    #         conexion = pyodbc.connect(
    #             'DRIVER={SQL Server};'
    #             'SERVER=DESKTOP-8L3U16R;'  
    #             'DATABASE=ObligatorioBD;'      
    #             'Trusted_Connection=yes;' 
    #         )
    #         return conexion
    #     except pyodbc.Error as e:
    #         print("Error al conectar con la base de datos:", e)
    #         return None
    def conectar_bd():
        try:
            #Conexion de TADEO D.
            conexion = pyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=LAPTOP-OMEVDG9L;'  
                'DATABASE=OBLIGATORIO;'      
                'Trusted_Connection=yes;' 
            )
            return conexion
        except pyodbc.Error as e:
            print("Error al conectar con la base de datos:", e)
            return None
        
        
        