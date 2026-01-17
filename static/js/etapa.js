document.addEventListener('DOMContentLoaded', async () => {
    await carregarEtapa();
    await carregarTarefas();
});

async function carregarEtapa() {
    try {
        const response = await fetch(`/etapa/api/${etapaId}`);
        const etapa = await response.json();
        
        document.getElementById('etapa-nome').textContent = etapa.nome;
        document.getElementById('responsavel-nome').textContent = etapa.responsavel;
        
        // Atualizar breadcrumb
        const breadcrumb = document.getElementById('breadcrumb');
        breadcrumb.innerHTML = `
            <a href="/">Dashboard</a> > 
            <a href="/departamento/${etapa.departamento_id}">Departamento Fiscal</a> > 
            <span>${etapa.nome}</span>
        `;
    } catch (error) {
        console.error('Erro ao carregar etapa:', error);
    }
}

async function carregarTarefas() {
    try {
        const response = await fetch(`/tarefa/api/etapa/${etapaId}`);
        const tarefas = await response.json();
        
        const container = document.getElementById('tarefas-lista');
        container.innerHTML = '';
        
        tarefas.forEach(tarefa => {
            const item = criarItemTarefa(tarefa);
            container.appendChild(item);
        });
    } catch (error) {
        console.error('Erro ao carregar tarefas:', error);
    }
}

function criarItemTarefa(tarefa) {
    const item = document.createElement('div');
    item.className = `tarefa-item ${tarefa.concluida ? 'concluida' : ''}`;
    item.id = `tarefa-${tarefa.id}`;
    
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.className = 'tarefa-checkbox';
    checkbox.checked = tarefa.concluida;
    checkbox.addEventListener('change', async (e) => {
        await marcarTarefa(tarefa.id, e.target.checked);
    });
    
    const descricao = document.createElement('span');
    descricao.className = 'tarefa-descricao';
    descricao.textContent = tarefa.descricao;
    
    item.appendChild(checkbox);
    item.appendChild(descricao);
    
    return item;
}

async function marcarTarefa(tarefaId, concluida) {
    try {
        const response = await fetch(`/tarefa/api/${tarefaId}/concluir`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ concluida })
        });
        
        if (response.ok) {
            const item = document.getElementById(`tarefa-${tarefaId}`);
            if (concluida) {
                item.classList.add('concluida');
            } else {
                item.classList.remove('concluida');
            }
        } else {
            console.error('Erro ao atualizar tarefa');
            // Reverter checkbox se falhar
            const checkbox = document.querySelector(`#tarefa-${tarefaId} .tarefa-checkbox`);
            checkbox.checked = !concluida;
        }
    } catch (error) {
        console.error('Erro ao marcar tarefa:', error);
        // Reverter checkbox se falhar
        const checkbox = document.querySelector(`#tarefa-${tarefaId} .tarefa-checkbox`);
        checkbox.checked = !concluida;
    }
}
