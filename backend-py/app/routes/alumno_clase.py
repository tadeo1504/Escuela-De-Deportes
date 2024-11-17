from flask import Blueprint, jsonify, request
from app.models.gestion_alumno_clase import GestionAlumnoClase

alumno_clase_bp = Blueprint('alumno-clase', __name__)

@alumno_clase_bp.route('/alumno-clase', methods=['POST'])
def vincular_alumno_clase():
    datos = request.get_json()
    ci_alumno = datos.get("ci_alumno")
    id_clase = datos.get("id_clase")
    id_equipamiento = datos.get("id_equipamiento")

    if not all([ci_alumno, id_clase, id_equipamiento]):
        return jsonify({"error": "Faltan datos para realizar el vínculo"}), 400

    try:
        GestionAlumnoClase.vincular_alumno_clase(ci_alumno, id_clase, id_equipamiento)
        return jsonify({"mensaje": "Alumno vinculado a la clase con éxito"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@alumno_clase_bp.route('/alumno-clase/<int:id_clase>', methods=['GET'])
def obtener_alumnos_clase(id_clase):
    try:
        alumnos = GestionAlumnoClase.ver_alumnos_clase(id_clase)
        return jsonify(alumnos), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500