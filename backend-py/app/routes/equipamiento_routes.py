
from flask import Blueprint, jsonify, request
from app.models.equipamiento import Equipamiento

equipamiento_bp = Blueprint('equipamiento', __name__)

@equipamiento_bp.route('/equipamiento', methods=['GET'])
def obtener_equipamiento():
    try:
        equipamiento = Equipamiento.verEquipamiento()
        return jsonify(equipamiento)
    except Exception as e:
        return jsonify({"error": f"Error interno: {e}"}), 500


@equipamiento_bp.route('/equipamiento', methods=['POST'])
def registrar_equipamiento():
    data = request.get_json()
    nombre = data.get('nombre')
    cantidad = data.get('cantidad')
    Equipamiento.altaEquipamiento(nombre, cantidad)
    return jsonify({"mensaje": "Equipamiento registrado exitosamente"}), 201

@equipamiento_bp.route('/equipamiento/<int:id>', methods=['DELETE'])
def eliminar_equipamiento(id):
    Equipamiento.bajaEquipamiento(id)
    return jsonify({"mensaje": "Equipamiento eliminado exitosamente"}), 200

@equipamiento_bp.route('/equipamiento/<int:id>', methods=['PUT'])
def modificar_equipamiento(id):
    data = request.get_json()
    nombre = data.get('nombre')
    cantidad = data.get('cantidad')
    Equipamiento.modificarEquipamiento(id, nombre, cantidad)
    return jsonify({"mensaje": "Equipamiento modificado exitosamente"}), 200
