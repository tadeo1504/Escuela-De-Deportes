# app/app.py

from flask import Flask
from .routes.alumnos_routes import alumnos_bp
# from app.routes.instructores_routes import instructores_bp
# from app.routes.clases_routes import clases_bp
# from app.routes.actividades_routes import actividades_bp
# Importa más blueprints si los tienes

def create_app():
    # Crea una instancia de la aplicación Flask
    app = Flask(__name__)
    
    # Configuración de la aplicación (si tienes configuraciones especiales)
    # app.config['DEBUG'] = True  # Ejemplo de configuración

    # Registrar los blueprints
    app.register_blueprint(alumnos_bp, url_prefix='/api')
    # app.register_blueprint(instructores_bp, url_prefix='/api')
    # app.register_blueprint(clases_bp, url_prefix='/api')
    # app.register_blueprint(actividades_bp, url_prefix='/api')
    # Registrar otros blueprints si es necesario

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
