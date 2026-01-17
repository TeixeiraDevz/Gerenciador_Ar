from flask import Blueprint, render_template, jsonify
from src.application.services.departamento_service import DepartamentoService

departamento_blueprint = Blueprint('departamento', __name__, url_prefix='/departamento')

@departamento_blueprint.route('/<int:departamento_id>')
def visualizar_departamento(departamento_id):
    return render_template('departamento.html', departamento_id=departamento_id)

@departamento_blueprint.route('/api/<int:departamento_id>', methods=['GET'])
def obter_departamento(departamento_id):
    service = DepartamentoService()
    departamento = service.obter_por_id(departamento_id)
    
    if not departamento:
        return jsonify({'error': 'Departamento não encontrado'}), 404
    
    return jsonify({
        'id': departamento.id,
        'nome': departamento.nome
    })

@departamento_blueprint.route('/api/listar', methods=['GET'])
def listar_departamentos():
    service = DepartamentoService()
    departamentos = service.listar_todos()
    
    return jsonify([{
        'id': d.id,
        'nome': d.nome
    } for d in departamentos])
