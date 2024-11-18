from flask import Blueprint, request, jsonify
from app.models.abm_instructores import ABMInstructores

# Creamos un Blueprint para las rutas de alumnos
instructores_bp = Blueprint('instructores', __name__)

# Endpoint para registrar un alumno
@instructores_bp.route('/instructores', methods=['POST'])
def alta_instructor():
    data = request.get_json()
    # Datos del alumno recibidos desde el body
    ci = data.get('ci')
    nombre = data.get('nombre')
    apellido = data.get('apellido')

    if not ci or not nombre or not apellido:
        return jsonify({"error": "Faltan datos necesarios"}), 400

    ABMInstructores.altaInstructor(ci, nombre, apellido)
    return jsonify({"message": "Instructor registrado con éxito"}), 201


# Endpoint para dar de baja a un alumno
@instructores_bp.route('/instructores/<ci>', methods=['DELETE'])
def baja_instructor(ci):
    try:
        ABMInstructores.bajaInstructor(ci)
        return jsonify({"message": "Instructor dado de baja con éxito"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@instructores_bp.route('/instructores/<ci>', methods=['PUT'])
def modificar_instructor(ci):
    data = request.get_json()
    nombre = data.get('nombre', '')
    apellido = data.get('apellido', '')

    ABMInstructores.modificarInstructor(ci, nombre, apellido)
    return jsonify({"message": "Datos del instructor actualizados con éxito"}), 200



# Endpoint para ver todos los alumnos
@instructores_bp.route('/instructores', methods=['GET'])
def ver_instructores():
    instructores = ABMInstructores.verInstructores()
    return jsonify({"instructores": instructores}), 200

# Endpoint para ver un alumno en específico
@instructores_bp.route('/instructores/<ci>', methods=['GET'])
def ver_instructor_ci(ci):
    instructor = ABMInstructores.verInstructorPorCI(ci)
    if instructor:
        return jsonify({"instructor": instructor}), 200
    return jsonify({"error": "Instructor no encontrado"}), 404