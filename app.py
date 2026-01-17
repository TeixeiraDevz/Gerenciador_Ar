from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

from src.infrastructure.database.database_config import init_db
from src.presentation.controllers.dashboard_controller import dashboard_blueprint
from src.presentation.controllers.departamento_controller import departamento_blueprint
from src.presentation.controllers.etapa_controller import etapa_blueprint
from src.presentation.controllers.tarefa_controller import tarefa_blueprint

app.register_blueprint(dashboard_blueprint)
app.register_blueprint(departamento_blueprint)
app.register_blueprint(etapa_blueprint)
app.register_blueprint(tarefa_blueprint)

# Inicializar banco de dados
init_db()


if __name__ == '__main__':
    # Configurações para desenvolvimento vs produção
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
