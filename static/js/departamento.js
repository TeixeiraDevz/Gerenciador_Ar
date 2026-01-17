document.addEventListener('DOMContentLoaded', async () => {
    await carregarDepartamento();
    await carregarEtapas();
});

async function carregarDepartamento() {
    try {
        const response = await fetch(`/departamento/api/${departamentoId}`);
        const data = await response.json();
        
        document.getElementById('departamento-nome').textContent = data.nome;
        document.getElementById('departamento-titulo').textContent = data.nome;
    } catch (error) {
        console.error('Erro ao carregar departamento:', error);
    }
}

async function carregarEtapas() {
    try {
        const response = await fetch(`/etapa/api/departamento/${departamentoId}`);
        const etapas = await response.json();
        
        const container = document.getElementById('etapas-container');
        container.innerHTML = '';
        
        etapas.forEach(etapa => {
            const card = criarCardEtapa(etapa);
            container.appendChild(card);
        });
    } catch (error) {
        console.error('Erro ao carregar etapas:', error);
    }
}

function criarCardEtapa(etapa) {
    const card = document.createElement('a');
    card.href = `/etapa/${etapa.id}`;
    card.className = 'etapa-card';
    
    card.innerHTML = `
        <h3>${etapa.nome}</h3>
        <p class="responsavel"><strong>Responsável:</strong> ${etapa.responsavel}</p>
        <div class="progress">
            <div class="progress-bar">
                <div class="progress-fill" style="width: 0%"></div>
            </div>
            <div class="progress-text">Carregando progresso...</div>
        </div>
    `;
    
    // Carregar progresso da etapa
    carregarProgressoEtapa(etapa.id, card);
    
    return card;
}

async function carregarProgressoEtapa(etapaId, cardElement) {
    try {
        const response = await fetch(`/tarefa/api/etapa/${etapaId}`);
        const tarefas = await response.json();
        
        const total = tarefas.length;
        const concluidas = tarefas.filter(t => t.concluida).length;
        const porcentagem = total > 0 ? Math.round((concluidas / total) * 100) : 0;
        
        const progressFill = cardElement.querySelector('.progress-fill');
        const progressText = cardElement.querySelector('.progress-text');
        
        progressFill.style.width = `${porcentagem}%`;
        progressText.textContent = `${concluidas} de ${total} tarefas concluídas (${porcentagem}%)`;
    } catch (error) {
        console.error('Erro ao carregar progresso da etapa:', error);
    }
}
