from flask import Blueprint, jsonify, request
from app.models.login import LoginUsuario

login_bp = Blueprint('auth', __name__)

@login_bp.route('/register', methods=['POST'])
def registrar():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    try:
        LoginUsuario.registrar_usuario(username, password)
        return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    try:
        if LoginUsuario.verificar_usuario(username, password):
            return jsonify({"mensaje": "Login exitoso"}), 200
        else:
            return jsonify({"error": "Credenciales inválidas"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 400
