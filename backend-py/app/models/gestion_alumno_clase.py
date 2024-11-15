from app.db_connection import DBConnection

class GestionAlumnoClase:
    @staticmethod
    def vincular_alumno_clase(ci_alumno, id_clase, id_equipamiento):
        conexion = DBConnection.conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            try:
                # Verificar si el alumno ya está registrado en la clase
                cursor.execute(
                    "SELECT COUNT(*) FROM alumno_clase WHERE ci_alumno = ? AND id_clase = ?", 
                    (ci_alumno, id_clase)
                )
                if cursor.fetchone()[0] > 0:
                    raise Exception("El alumno ya está registrado en esta clase.")
                
                # Insertar el vínculo
                cursor.execute(
                    "INSERT INTO alumno_clase (ci_alumno, id_clase, id_equipamiento) VALUES (?, ?, ?)",
                    (ci_alumno, id_clase, id_equipamiento)
                )
                conexion.commit()
            except Exception as e:
                raise Exception(f"Error al vincular al alumno con la clase: {e}")
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def ver_alumnos_clase(id_clase):
        conexion = DBConnection.conectar_bd()
        alumnos = []
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute(
                    "SELECT a.ci, a.nombre, a.apellido, ac.id_equipamiento "
                    "FROM alumno_clase ac "
                    "JOIN alumnos a ON ac.ci_alumno = a.ci "
                    "WHERE ac.id_clase = ?",
                    (id_clase,)
                )
                alumnos = [
                    {
                        "ci": row[0],
                        "nombre": row[1],
                        "apellido": row[2],
                        "id_equipamiento": row[3]
                    }
                    for row in cursor.fetchall()
                ]
            except Exception as e:
                raise Exception(f"Error al obtener los alumnos de la clase: {e}")
            finally:
                cursor.close()
                conexion.close()
        return alumnos
