from flask import Blueprint, render_template, jsonify
from src.application.services.etapa_service import EtapaService

etapa_blueprint = Blueprint('etapa', __name__, url_prefix='/etapa')

@etapa_blueprint.route('/<int:etapa_id>')
def visualizar_etapa(etapa_id):
    return render_template('etapa.html', etapa_id=etapa_id)

@etapa_blueprint.route('/api/departamento/<int:departamento_id>', methods=['GET'])
def listar_etapas_por_departamento(departamento_id):
    service = EtapaService()
    etapas = service.listar_por_departamento(departamento_id)
    
    return jsonify([{
        'id': e.id,
        'numero': e.numero,
        'nome': e.nome,
        'responsavel': e.responsavel,
        'departamento_id': e.departamento_id
    } for e in etapas])

@etapa_blueprint.route('/api/<int:etapa_id>', methods=['GET'])
def obter_etapa(etapa_id):
    service = EtapaService()
    etapa = service.obter_por_id(etapa_id)
    
    if not etapa:
        return jsonify({'error': 'Etapa não encontrada'}), 404
    
    return jsonify({
        'id': etapa.id,
        'numero': etapa.numero,
        'nome': etapa.nome,
        'responsavel': etapa.responsavel,
        'departamento_id': etapa.departamento_id
    })
