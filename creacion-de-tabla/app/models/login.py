from app.db_connection import DBConnection
import bcrypt  # Para cifrar y verificar contraseñas

class LoginUsuario:
    @staticmethod
    def registrar_usuario(username, password):
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            # Cifrar la contraseña y convertirla a texto para almacenar
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            cursor.execute("INSERT INTO login (username, password) VALUES (?, ?)", 
                           (username, hashed_password))
            conexion.commit()
        except Exception as e:
            raise Exception(f"Error al registrar el usuario: {e}")
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def verificar_usuario(username, password):
        conexion = DBConnection.conectar_bd()
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT password FROM login WHERE username = ?", (username,))
            result = cursor.fetchone()

            if not result:
                raise Exception("Usuario no encontrado")

            # Recuperar el hash almacenado como texto
            hashed_password = result[0]

            # Comparar la contraseña ingresada con el hash almacenado
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                return True
            else:
                return False
        except Exception as e:
            raise Exception(f"Error al verificar el usuario: {e}")
        finally:
            cursor.close()
            conexion.close()
