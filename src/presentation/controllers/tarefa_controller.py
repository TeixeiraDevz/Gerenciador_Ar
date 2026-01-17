from flask import Blueprint, jsonify, request
from src.application.services.tarefa_service import TarefaService

tarefa_blueprint = Blueprint('tarefa', __name__, url_prefix='/tarefa')

@tarefa_blueprint.route('/api/etapa/<int:etapa_id>', methods=['GET'])
def listar_tarefas_por_etapa(etapa_id):
    service = TarefaService()
    tarefas = service.listar_por_etapa(etapa_id)
    
    return jsonify([{
        'id': t.id,
        'descricao': t.descricao,
        'concluida': t.concluida,
        'etapa_id': t.etapa_id
    } for t in tarefas])

@tarefa_blueprint.route('/api/<int:tarefa_id>/concluir', methods=['PUT'])
def marcar_concluida(tarefa_id):
    data = request.get_json()
    concluida = data.get('concluida', True)
    
    service = TarefaService()
    service.atualizar_conclusao(tarefa_id, concluida)
    
    return jsonify({'success': True, 'message': 'Tarefa atualizada com sucesso'})
