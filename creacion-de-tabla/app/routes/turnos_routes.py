from flask import Blueprint, jsonify, request
from app.models.abm_turnos import ABMTurnos

turnos_bp = Blueprint('turnos', __name__)

@turnos_bp.route('/turnos', methods=['GET'])
def obtener_turnos():
    turnos = ABMTurnos.verTurnos()
    print(turnos)
    return jsonify(turnos)

@turnos_bp.route('/turnos', methods=['POST'])
def agregar_turno():
    data = request.get_json()
    id_turno = data.get('id')
    hora_inicio = data.get('hora_inicio')
    hora_final = data.get('hora_final')

    if not id_turno or not hora_inicio or not hora_final:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    ABMTurnos.altaTurnos(id_turno, hora_inicio, hora_final)
    return jsonify({"mensaje": "Turno agregado exitosamente"}), 201

@turnos_bp.route('/turnos/<int:id>', methods=['PUT'])
def modificar_turno(id):
    data = request.get_json()
    hora_inicio = data.get('hora_inicio')
    hora_final = data.get('hora_final')

    ABMTurnos.modificarTurnos(id, hora_inicio, hora_final)
    return jsonify({"mensaje": "Turno modificado exitosamente"}), 200

@turnos_bp.route('/turnos/<int:id>', methods=['DELETE'])
def eliminar_turno(id):
    ABMTurnos.bajaTurnos(id)
    return jsonify({"mensaje": "Turno eliminado exitosamente"}), 200
