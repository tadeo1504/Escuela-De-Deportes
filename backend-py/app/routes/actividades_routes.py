from flask import Blueprint, jsonify, request
from app.models.modificaciones_actividades import ModificacionesActividades

actividades_bp = Blueprint('actividades', __name__)

@actividades_bp.route('/actividades', methods=['GET'])
def obtener_actividades():
    actividades = ModificacionesActividades.verDeportes()
    return jsonify(actividades)

@actividades_bp.route('/actividades', methods=['POST'])
def agregar_actividad():
    data = request.get_json()
    nuevo_deporte = data.get('nombre')
    costo = data.get('costo')

    if not nuevo_deporte or not costo:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    ModificacionesActividades.agregarDeportes( nuevo_deporte, costo)
    return jsonify({"mensaje": "Actividad agregada exitosamente"}), 201

@actividades_bp.route('/actividades/<int:id>', methods=['DELETE'])
def eliminar_actividad(id):
    ModificacionesActividades.eliminarDeportes(id)
    return jsonify({"mensaje": "Actividad eliminada exitosamente"}), 200

@actividades_bp.route('/actividades/<int:id>', methods=['PUT'])
def modificar_actividad(id):
    data = request.get_json()
    nombre = data.get('nombre')
    costo = data.get('costo')

    if not nombre or not costo:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    ModificacionesActividades.modificarDeportes(id, nombre, costo)
    return jsonify({"mensaje": "Actividad modificada exitosamente"}), 200
