from flask import Flask, jsonify, request, Blueprint
from datetime import date
from app.models.gestion_clases import GestionClases

clases_bp = Blueprint('clases', __name__)

@clases_bp.route('/clases', methods=['GET'])
def obtener_clases():
    clases = GestionClases.verClases()
    return jsonify(clases)

from flask import jsonify, request
from datetime import date

@clases_bp.route('/clases/<int:id_clase>', methods=['PUT'])
def modificar_clase(id_clase):
    nuevos_datos = request.get_json()

    try:
        clase = GestionClases.obtener_clase_por_id(id_clase)
        if not clase:
            return jsonify({"error": "Clase no encontrada"}), 404

        if clase["dictada"] == str(date.today()):
            return jsonify({"error": "La clase no puede ser modificada el día en que se dicta."}), 400

        GestionClases.actualizar_clase(id_clase, nuevos_datos)
        return jsonify({"mensaje": "Clase modificada exitosamente"}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Error interno: " + str(e)}), 500


@clases_bp.route('/clases', methods=['POST'])
def agregar_clase():
    datos = request.get_json()
    ci_instructor = datos.get("ci_instructor")
    id_actividad = datos.get("id_actividad")
    id_turno = datos.get("id_turno")
    dictada = datos.get("dictada")

    try:
        GestionClases.crearClase(ci_instructor, id_actividad, id_turno, dictada)
        return jsonify({"mensaje": "Clase creada con éxito"}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Error interno: " + str(e)}), 500