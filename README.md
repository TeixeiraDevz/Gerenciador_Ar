# Gerenciador Ar

Sistema de gerenciamento de tarefas focado em processos fiscais e contábeis, permitindo o acompanhamento de etapas e responsabilidades por departamento.

## 🎯 Funcionalidades

- **Dashboard**: Visão geral de todas as tarefas do sistema com estatísticas por responsável
- **Departamento Fiscal**: Gerenciamento das 7 etapas fiscais
- **Etapas**: Cada etapa possui um responsável específico:
  - 1ª e 2ª Etapa: **Jucier**
  - 3ª, 5ª e 6ª Etapa: **Altemar**
  - 4ª Etapa: **Mila**
  - 7ª Etapa: **Andréa**
- **Tarefas**: Marcação de tarefas como concluídas/pendentes com interface neon moderna

## 🛠️ Tecnologias

- **Backend**: Flask (Python 3.11+)
- **Frontend**: HTML, CSS (neon theme), JavaScript
- **Banco de Dados**: SQLite (pode ser migrado para PostgreSQL em produção)
- **Arquitetura**: Clean Architecture em camadas (Domain, Application, Infrastructure, Presentation)

## 📦 Instalação

### Pré-requisitos

- Python 3.11 ou superior
- Git (para versionamento)

### Passos de Instalação

1. **Clone o repositório**
   ```powershell
   git clone <seu-repositorio>
   cd "Gerenciador Ar"
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Instale as dependências**
   ```powershell
   python -m pip install -r requirements.txt
   ```

4. **Execute o projeto**
   ```powershell
   python app.py
   ```

5. **Acesse no navegador**
   ```
   http://localhost:5000
   ```

## 🚀 Deploy Automatizado

### Usando o Script Automatizado

Execute o script `deploy.ps1` para automatizar todo o processo:

```powershell
.\deploy.ps1
```

O script:
- ✅ Verifica se o Git está inicializado
- ✅ Verifica arquivos que não devem ser commitados
- ✅ Faz commit automático
- ✅ Faz push para o repositório remoto (se configurado)

### Deploy Manual

#### Opção 1: Render.com (Recomendado)

1. Acesse https://render.com e faça login
2. Clique em "New +" → "Web Service"
3. Conecte seu repositório GitHub/GitLab
4. Configure:
   - **Name:** `gerenciador-ar`
   - **Start Command:** `gunicorn wsgi:app`
   - **Build Command:** `pip install -r requirements.txt`
   - **Runtime:** Python 3
5. Clique em "Create Web Service"
6. Aguarde o deploy (2-5 minutos)

**Variáveis de Ambiente (opcional):**
- `SECRET_KEY`: (gere uma chave secreta)
- `FLASK_DEBUG`: `False`

#### Opção 2: Heroku

```powershell
heroku login
heroku create gerenciador-ar
heroku config:set SECRET_KEY=sua-chave-secreta
heroku config:set FLASK_DEBUG=False
git push heroku main
```

#### Opção 3: Railway

1. Acesse https://railway.app
2. Novo Projeto → Deploy from GitHub
3. Selecione seu repositório
4. Railway detecta automaticamente e faz deploy

## 📂 Estrutura do Projeto

```
Gerenciador Ar/
├── app.py                 # Aplicação Flask principal
├── wsgi.py                # Entrada WSGI para produção
├── requirements.txt       # Dependências Python
├── Procfile              # Configuração para Heroku/Render
├── deploy.ps1            # Script automatizado de deploy
├── src/
│   ├── domain/           # Entidades e DTOs
│   ├── application/      # Serviços de negócio
│   ├── infrastructure/   # Repositórios, Mappers, Database
│   └── presentation/     # Controllers (Flask Blueprints)
├── templates/            # Templates HTML
├── static/               # CSS e JavaScript
└── gerenciador_ar.db     # Banco de dados SQLite (gerado automaticamente)
```

## 🗄️ Banco de Dados

O banco de dados SQLite (`gerenciador_ar.db`) é criado automaticamente na primeira execução, junto com:
- Departamento Fiscal
- 7 etapas configuradas
- Tarefas padrão para cada etapa

**Para produção escalável**, migre para PostgreSQL:
1. Adicione PostgreSQL no Render/Heroku
2. Use a `DATABASE_URL` fornecida
3. Instale `psycopg2-binary` no requirements.txt

## 🔧 Configuração Git

O projeto inclui `.gitignore` configurado para ignorar:
- Banco de dados local (`*.db`)
- Ambiente virtual (`venv/`)
- Cache Python (`__pycache__/`)
- Arquivos de sistema e editor

**Verificar arquivos antes de commit:**
```powershell
git status
```

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError"
**Solução:** Instale as dependências: `python -m pip install -r requirements.txt`

### Erro: "Port already in use"
**Solução:** Altere a porta no `app.py` ou mate o processo usando a porta 5000

### CSS/JS não carregam
**Solução:** Limpe o cache do navegador (Ctrl+F5) ou verifique se a pasta `static/` está no projeto

### Banco de dados não inicializa
**Solução:** Verifique permissões de escrita na pasta do projeto

## 📊 Estrutura de Dados

### Departamentos
- ID, Nome

### Etapas
- ID, Número, Nome, Responsável, Departamento ID

### Tarefas
- ID, Descrição, Concluída (boolean), Etapa ID

## 🎨 Design

Interface moderna com tema neon:
- Fundo azul escuro gradiente
- Elementos neon (cian, azul, roxo)
- Animações suaves e hover effects
- Layout responsivo

## 📝 Desenvolvimento

O projeto segue princípios SOLID e arquitetura em camadas:
- Separação de responsabilidades
- Uso de DTOs para comunicação entre camadas
- Mappers para conversão Entity ↔ DTO
- Injeção de dependência
- Repositórios para acesso a dados

## 📄 Licença

Este projeto é proprietário.

## 🆘 Suporte

Para problemas:
1. Verifique os logs no terminal
2. Consulte a seção Troubleshooting
3. Verifique se todas as dependências estão instaladas

---

**Desenvolvido com ❤️ para gerenciamento eficiente de tarefas fiscais**
