document.addEventListener('DOMContentLoaded', async () => {
    await carregarResumo();
});

async function carregarResumo() {
    try {
        const response = await fetch('/api/dashboard/resumo');
        const data = await response.json();
        
        // Atualizar estatísticas principais
        document.getElementById('total-tarefas').textContent = data.total_tarefas;
        document.getElementById('tarefas-concluidas').textContent = data.tarefas_concluidas;
        document.getElementById('tarefas-pendentes').textContent = data.tarefas_pendentes;
        document.getElementById('porcentagem-concluidas').textContent = `${data.porcentagem_concluida}% concluído`;
        
        // Carregar resumo por responsável
        carregarResumoResponsaveis(data.resumo_responsaveis);
        
        // Carregar resumo por etapa
        carregarResumoEtapas(data.resumo_etapas);
    } catch (error) {
        console.error('Erro ao carregar resumo:', error);
    }
}

function carregarResumoResponsaveis(responsaveis) {
    const container = document.getElementById('resumo-responsaveis');
    container.innerHTML = '';
    
    if (!responsaveis || responsaveis.length === 0) {
        container.innerHTML = '<p style="color: #b0b0b0;">Nenhum responsável encontrado.</p>';
        return;
    }
    
    responsaveis.forEach(responsavel => {
        const card = criarCardResponsavel(responsavel);
        container.appendChild(card);
    });
}

function criarCardResponsavel(responsavel) {
    const card = document.createElement('div');
    card.className = 'responsavel-card';
    
    card.innerHTML = `
        <div class="responsavel-header">
            <h4>${responsavel.nome}</h4>
            <span class="badge-etapas">${responsavel.num_etapas} etapa(s)</span>
        </div>
        <div class="responsavel-stats">
            <div class="stat-item">
                <span class="stat-label">Total:</span>
                <span class="stat-value">${responsavel.total}</span>
            </div>
            <div class="stat-item success">
                <span class="stat-label">Concluídas:</span>
                <span class="stat-value">${responsavel.concluidas}</span>
            </div>
            <div class="stat-item warning">
                <span class="stat-label">Pendentes:</span>
                <span class="stat-value">${responsavel.pendentes}</span>
            </div>
        </div>
        <div class="progress">
            <div class="progress-bar">
                <div class="progress-fill" style="width: ${responsavel.porcentagem}%"></div>
            </div>
            <div class="progress-text">${Math.round(responsavel.porcentagem)}% concluído</div>
        </div>
    `;
    
    return card;
}

function carregarResumoEtapas(etapas) {
    const container = document.getElementById('resumo-etapas');
    container.innerHTML = '';
    
    if (!etapas || etapas.length === 0) {
        container.innerHTML = '<p style="color: #b0b0b0;">Nenhuma etapa encontrada.</p>';
        return;
    }
    
    // Ordenar etapas por número
    etapas.sort((a, b) => a.numero - b.numero);
    
    etapas.forEach(etapa => {
        const card = criarCardResumoEtapa(etapa);
        container.appendChild(card);
    });
}

function criarCardResumoEtapa(etapa) {
    const card = document.createElement('a');
    card.href = `/etapa/${etapa.id}`;
    card.className = 'resumo-etapa-card';
    
    const porcentagem = etapa.total > 0 
        ? Math.round((etapa.concluidas / etapa.total) * 100) 
        : 0;
    
    card.innerHTML = `
        <h3>${etapa.etapa}</h3>
        <p class="responsavel-info-text">
            <strong>Responsável:</strong> <span style="color: var(--neon-blue);">${etapa.responsavel}</span>
        </p>
        <div class="progress">
            <div class="progress-bar">
                <div class="progress-fill" style="width: ${porcentagem}%"></div>
            </div>
            <div class="progress-text">
                ${etapa.concluidas} de ${etapa.total} tarefas concluídas (${porcentagem}%)
            </div>
        </div>
        <div class="info">
            <span>✅ ${etapa.concluidas}</span>
            <span>⏳ ${etapa.pendentes}</span>
        </div>
    `;
    
    return card;
}
