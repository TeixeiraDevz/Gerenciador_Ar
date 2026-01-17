import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'gerenciador_ar.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Criar tabela de departamentos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS departamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        )
    ''')
    
    # Criar tabela de etapas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS etapas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER NOT NULL,
            nome TEXT NOT NULL,
            responsavel TEXT NOT NULL,
            departamento_id INTEGER NOT NULL,
            FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
        )
    ''')
    
    # Criar tabela de tarefas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            concluida BOOLEAN DEFAULT 0,
            etapa_id INTEGER NOT NULL,
            FOREIGN KEY (etapa_id) REFERENCES etapas(id)
        )
    ''')
    
    conn.commit()
    
    # Inicializar dados se não existirem
    cursor.execute('SELECT COUNT(*) FROM departamentos')
    if cursor.fetchone()[0] == 0:
        # Inserir Departamento Fiscal
        cursor.execute('INSERT INTO departamentos (nome) VALUES (?)', ('Fiscal',))
        conn.commit()
        
        # Obter o ID do departamento Fiscal
        cursor.execute('SELECT id FROM departamentos WHERE nome = ?', ('Fiscal',))
        fiscal_id = cursor.fetchone()[0]
        
        # Inserir as 7 etapas do Departamento Fiscal
        etapas = [
            (1, '1ª Etapa - Municipal', 'Jucier', fiscal_id),
            (2, '2ª Etapa - Estadual', 'Jucier', fiscal_id),
            (3, '3ª Etapa', 'Altemar', fiscal_id),
            (4, '4ª Etapa - Apuração Simples Nacional', 'Mila', fiscal_id),
            (5, '5ª Etapa - Apuração Impostos', 'Altemar', fiscal_id),
            (6, '6ª Etapa - Entrega Declarações', 'Altemar', fiscal_id),
            (7, '7ª Etapa', 'Andréa', fiscal_id)
        ]
        
        cursor.executemany('''
            INSERT INTO etapas (numero, nome, responsavel, departamento_id)
            VALUES (?, ?, ?, ?)
        ''', etapas)
        conn.commit()
        
        # Inserir tarefas padrão para cada etapa baseado nas imagens
        cursor.execute('SELECT id, numero FROM etapas WHERE departamento_id = ? ORDER BY numero', (fiscal_id,))
        etapas_data = cursor.fetchall()
        
        tarefas_por_etapa = {
            1: [
                'Fechamento ISS do mês anterior',
                'XML Tipo de Nota: EMITIDAS',
                'XML Tipo de Nota: RECEBIDAS',
                'Guia ISSQN',
                'Guia ISSRF (Cliente Substituto)',
                'Livro Fiscal Serviço Prestado-ISSQN',
                'Relatório de notas fiscais recebidas'
            ],
            2: [
                'XML Recebidos e Relatório Excel - NF-e',
                'XML Recebidos e Relatório Excel - NFC-e',
                'XML Recebidos e Relatório Excel - CT-e como Tomador',
                'XML Emitidos e Relatório Excel - NF-e',
                'XML Emitidos e Relatório Excel - NFC-e',
                'XML Emitidos e Relatório Excel - CT-e Emitidos'
            ],
            3: [
                'Importar arquivos XML MUNICIPAL e ESTADUAL para sistema Domínio',
                'Identificar notas canceladas (Prestador/Tomador)',
                'Unicargo incluir na entrada conta Energia enviada pelo cliente',
                'Escriturar notas de serviços tomados outros Municípios',
                'Gerar parcelas recebimento para cliente regime de caixa'
            ],
            4: [
                'PGDAS Simples Nacional',
                'Guia Simples Nacional'
            ],
            5: [
                'ISS',
                'ICMS',
                'PIS',
                'COFINS',
                'CSLL',
                'IRPJ e Adicional'
            ],
            6: [
                'CSR',
                'INSS Retido',
                'DAM Simplificada',
                'EFD-ICMS',
                'EFD-Contribuições',
                'EFD-Reinf',
                'DIRBI',
                'DCTF'
            ],
            7: [
                'Envio guias Impostos para Clientes',
                'Salvar Livros fiscais (Entrada/Saida/Serviços/Apuração)',
                'Salvar resumo dos impostos',
                'Importação da Escrita Fiscal para a Contabilidade'
            ]
        }
        
        for etapa_row in etapas_data:
            etapa_id, numero = etapa_row
            if numero in tarefas_por_etapa:
                tarefas = tarefas_por_etapa[numero]
                for tarefa_desc in tarefas:
                    cursor.execute('''
                        INSERT INTO tarefas (descricao, concluida, etapa_id)
                        VALUES (?, 0, ?)
                    ''', (tarefa_desc, etapa_id))
        
        conn.commit()
    
    conn.close()
