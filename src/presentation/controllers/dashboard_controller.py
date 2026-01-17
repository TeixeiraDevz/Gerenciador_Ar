from flask import Blueprint, render_template, jsonify
from src.application.services.tarefa_service import TarefaService
from src.application.services.etapa_service import EtapaService
from src.application.services.departamento_service import DepartamentoService

dashboard_blueprint = Blueprint('dashboard', __name__)

@dashboard_blueprint.route('/')
def index():
    return render_template('dashboard.html')

@dashboard_blueprint.route('/api/dashboard/resumo', methods=['GET'])
def obter_resumo():
    tarefa_service = TarefaService()
    etapa_service = EtapaService()
    departamento_service = DepartamentoService()
    
    todas_tarefas = tarefa_service.listar_todas()
    departamentos = departamento_service.listar_todos()
    
    total_tarefas = len(todas_tarefas)
    tarefas_concluidas = sum(1 for t in todas_tarefas if t.concluida)
    tarefas_pendentes = total_tarefas - tarefas_concluidas
    porcentagem_concluida = (tarefas_concluidas / total_tarefas * 100) if total_tarefas > 0 else 0
    
    resumo_etapas = []
    resumo_departamentos = []
    resumo_responsaveis = {}
    
    for departamento in departamentos:
        etapas = etapa_service.listar_por_departamento(departamento.id)
        departamento_tarefas = []
        departamento_concluidas = 0
        departamento_total = 0
        
        for etapa in etapas:
            tarefas_etapa = [t for t in todas_tarefas if t.etapa_id == etapa.id]
            total_etapa = len(tarefas_etapa)
            concluidas_etapa = sum(1 for t in tarefas_etapa if t.concluida)
            
            departamento_total += total_etapa
            departamento_concluidas += concluidas_etapa
            departamento_tarefas.extend(tarefas_etapa)
            
            # Resumo por responsável
            if etapa.responsavel not in resumo_responsaveis:
                resumo_responsaveis[etapa.responsavel] = {
                    'total': 0,
                    'concluidas': 0,
                    'etapas': []
                }
            
            resumo_responsaveis[etapa.responsavel]['total'] += total_etapa
            resumo_responsaveis[etapa.responsavel]['concluidas'] += concluidas_etapa
            resumo_responsaveis[etapa.responsavel]['etapas'].append(etapa.nome)
            
            resumo_etapas.append({
                'id': etapa.id,
                'etapa': etapa.nome,
                'numero': etapa.numero,
                'responsavel': etapa.responsavel,
                'total': total_etapa,
                'concluidas': concluidas_etapa,
                'pendentes': total_etapa - concluidas_etapa,
                'departamento_id': departamento.id
            })
        
        resumo_departamentos.append({
            'id': departamento.id,
            'nome': departamento.nome,
            'total': departamento_total,
            'concluidas': departamento_concluidas,
            'pendentes': departamento_total - departamento_concluidas,
            'porcentagem': (departamento_concluidas / departamento_total * 100) if departamento_total > 0 else 0
        })
    
    # Converter dicionário de responsáveis em lista
    resumo_responsaveis_lista = [
        {
            'nome': nome,
            'total': dados['total'],
            'concluidas': dados['concluidas'],
            'pendentes': dados['total'] - dados['concluidas'],
            'porcentagem': (dados['concluidas'] / dados['total'] * 100) if dados['total'] > 0 else 0,
            'num_etapas': len(dados['etapas'])
        }
        for nome, dados in resumo_responsaveis.items()
    ]
    
    return jsonify({
        'total_tarefas': total_tarefas,
        'tarefas_concluidas': tarefas_concluidas,
        'tarefas_pendentes': tarefas_pendentes,
        'porcentagem_concluida': round(porcentagem_concluida, 1),
        'resumo_departamentos': resumo_departamentos,
        'resumo_etapas': resumo_etapas,
        'resumo_responsaveis': resumo_responsaveis_lista
    })
