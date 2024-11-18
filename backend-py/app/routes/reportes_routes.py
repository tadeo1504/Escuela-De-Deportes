from flask import Blueprint, jsonify
from app.db_connection import DBConnection

reportes_bp = Blueprint('reportes', __name__)

@reportes_bp.route('/reportes/ingresos-actividades', methods=['GET'])
def ingresos_actividades():
    conexion = DBConnection.conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                SELECT 
                    a.descripcion AS actividad,
                    SUM(e.costo) AS ingresos_totales
                FROM 
                    actividades a
                LEFT JOIN 
                    equipamiento e ON a.id = e.id_actividad
                GROUP BY 
                    a.descripcion
                ORDER BY 
                    ingresos_totales DESC;
            """)
            resultados = cursor.fetchall()
            return jsonify([
                {"actividad": row[0], "ingresos_totales": row[1]} for row in resultados
            ]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conexion.close()

@reportes_bp.route('/reportes/alumnos-actividades', methods=['GET'])
def alumnos_actividades():
    conexion = DBConnection.conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                SELECT 
                    a.descripcion AS actividad,
                    COUNT(ac.ci_alumno) AS alumnos_totales
                FROM 
                    actividades a
                JOIN 
                    clase c ON a.id = c.id_actividad
                JOIN 
                    alumno_clase ac ON c.id = ac.id_clase
                GROUP BY 
                    a.descripcion
                ORDER BY 
                    alumnos_totales DESC;
            """)
            resultados = cursor.fetchall()
            return jsonify([
                {"actividad": row[0], "alumnos_totales": row[1]} for row in resultados
            ]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conexion.close()

@reportes_bp.route('/reportes/turnos-dictados', methods=['GET'])
def turnos_dictados():
    conexion = DBConnection.conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                SELECT 
                    t.hora_inicio AS inicio,
                    t.hora_final AS fin,
                    COUNT(c.id) AS clases_totales
                FROM 
                    turnos t
                JOIN 
                    clase c ON t.id = c.id_turno
                GROUP BY 
                    t.hora_inicio, t.hora_final, t.id
                ORDER BY 
                    clases_totales DESC;
            """)
            resultados = cursor.fetchall()
            return jsonify([
                {"inicio": row[0], "fin": row[1], "clases_totales": row[2],} for row in resultados
            ]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conexion.close()
