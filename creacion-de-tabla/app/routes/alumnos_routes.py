from flask import Blueprint, request, jsonify
from app.models.abm_alumnos import ABMAlumnos

# Creamos un Blueprint para las rutas de alumnos
alumnos_bp = Blueprint('alumnos', __name__)

# Endpoint para registrar un alumno
@alumnos_bp.route('/alumnos', methods=['POST'])
def alta_alumno():
    data = request.get_json()
    # Datos del alumno recibidos desde el body
    ci = data.get('ci')
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    fecha_nacimiento = data.get('fecha_nacimiento')

    if not ci or not nombre or not apellido or not fecha_nacimiento:
        return jsonify({"error": "Faltan datos necesarios"}), 400

    ABMAlumnos.altaAlumno(ci, nombre, apellido, fecha_nacimiento)
    return jsonify({"message": "Alumno registrado con éxito"}), 201


# Endpoint para dar de baja a un alumno
@alumnos_bp.route('/alumnos/<ci>', methods=['DELETE'])
def baja_alumno(ci):
    ABMAlumnos.bajaAlumno(ci)
    return jsonify({"message": "Alumno dado de baja con éxito"}), 200


# Endpoint para modificar los datos de un alumno
@alumnos_bp.route('/alumnos/<ci>', methods=['PUT'])
def modificar_alumno(ci):
    data = request.get_json()
    nuevo_nombre = data.get('nuevo_nombre', '')
    nuevo_apellido = data.get('nuevo_apellido', '')

    ABMAlumnos.modificarAlumno(ci, nuevo_nombre, nuevo_apellido)
    return jsonify({"message": "Datos del alumno actualizados con éxito"}), 200


# Endpoint para ver todos los alumnos
@alumnos_bp.route('/alumnos', methods=['GET'])
def ver_alumnos():
    alumnos = ABMAlumnos.verAlumnos()
    return jsonify({"alumnos": alumnos}), 200

# Endpoint para ver un alumno en específico
@alumnos_bp.route('/alumnos/<ci>', methods=['GET'])
def ver_alumno_ci(ci):
    alumno = ABMAlumnos.verAlumnoPorCI(ci)
    if alumno:
        return jsonify({"alumnos": alumno}), 200
    return jsonify({"error": "Alumno no encontrado"}), 404
