# 🚀 Guia de Deploy no Vercel - Gerenciador Ar

## 🔍 Solução para Erro de Conexão com Repositório

Se você está recebendo o erro:
```
Error: Failed to connect TeixeiraDevz/Gerenciador_Ar to project
```

Siga os passos abaixo:

### ✅ Passo 1: Verificar Permissões no GitHub

1. Acesse https://github.com/settings/applications
2. Vá em "Authorized GitHub Apps" ou "OAuth Apps"
3. Verifique se o Vercel está autorizado
4. Se não estiver, autorize o Vercel novamente

### ✅ Passo 2: Verificar Nome do Repositório

Certifique-se que o nome do repositório está correto:
- **Formato esperado:** `TeixeiraDevz/Gerenciador_Ar`
- **Case-sensitive:** Certifique-se que as maiúsculas/minúsculas estão corretas

### ✅ Passo 3: Verificar Se o Repositório Existe

1. Acesse: https://github.com/TeixeiraDevz/Gerenciador_Ar
2. Verifique se o repositório existe e você tem acesso
3. Se for privado, certifique-se que o Vercel tem permissão

### ✅ Passo 4: Reconectar no Vercel

**Opção A: Via Dashboard**

1. Acesse https://vercel.com/dashboard
2. Vá em **Settings** → **Git**
3. Clique em **Disconnect** no repositório (se já estiver conectado)
4. Clique em **Connect Git Repository**
5. Autorize o GitHub novamente se necessário
6. Selecione o repositório `TeixeiraDevz/Gerenciador_Ar`

**Opção B: Criar Novo Projeto**

1. Acesse https://vercel.com/new
2. Selecione **Import Git Repository**
3. Autorize o GitHub se necessário
4. Procure por `Gerenciador_Ar` ou `TeixeiraDevz/Gerenciador_Ar`
5. Clique em **Import**

### ✅ Passo 5: Deploy Manual (Alternativa)

Se ainda não funcionar, faça deploy manualmente:

#### Via Vercel CLI

```powershell
# 1. Instalar Vercel CLI (se ainda não tiver)
npm install -g vercel

# 2. Login no Vercel
vercel login

# 3. Navegar até a pasta do projeto
cd "C:\Users\Andrea\OneDrive\Documentos\Gerenciador Ar"

# 4. Deploy
vercel

# 5. Responder as perguntas:
# - Set up and deploy? Y
# - Which scope? (seu usuário/team)
# - Link to existing project? N (ou Y se já tiver um projeto)
# - Project name? gerenciador-ar
# - Directory? ./
# - Override settings? N

# 6. Deploy em produção
vercel --prod
```

#### Via GitHub Actions (Opcional)

Crie um arquivo `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Vercel
on:
  push:
    branches: [ main ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.ORG_ID }}
          vercel-project-id: ${{ secrets.PROJECT_ID }}
```

---

## 📋 Checklist de Troubleshooting

- [ ] Repositório existe no GitHub
- [ ] Você tem acesso ao repositório
- [ ] Vercel está autorizado no GitHub
- [ ] Nome do repositório está correto (case-sensitive)
- [ ] Repositório não está vazio (tem pelo menos um commit)
- [ ] Branch `main` ou `master` existe

---

## 🔧 Configurações Importantes

### Variáveis de Ambiente no Vercel

Após conectar o repositório, configure as variáveis:

1. Vá em **Settings** → **Environment Variables**
2. Adicione:
   - `SECRET_KEY`: (gere uma chave secreta)
   - `FLASK_DEBUG`: `False`

### Gerar SECRET_KEY

```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## 🚀 Depois do Deploy

1. **Verificar Deploy**
   - Acesse o dashboard do Vercel
   - Veja os logs de deploy
   - Verifique se não há erros

2. **Testar Aplicação**
   - Acesse a URL fornecida pelo Vercel
   - Exemplo: `https://gerenciador-ar.vercel.app`

3. **Configurar Domínio (Opcional)**
   - Settings → Domains
   - Adicione seu domínio personalizado

---

## 📞 Se Ainda Não Funcionar

1. **Verificar Logs no Vercel**
   - Vá em Deployments → Clique no último deploy → Ver logs

2. **Testar Localmente**
   ```powershell
   vercel dev
   ```

3. **Verificar vercel.json**
   - Certifique-se que `vercel.json` está no repositório
   - Certifique-se que está na raiz do projeto

4. **Verificar requirements.txt**
   - Certifique-se que todas as dependências estão listadas

---

## 💡 Dicas

- Se o repositório for privado, certifique-se que sua conta Vercel tem acesso
- Para repositórios da organização, pode precisar de permissões especiais
- Sempre faça commit e push antes de tentar conectar no Vercel

---

**Pronto!** Após seguir estes passos, o deploy no Vercel deve funcionar. 🎉
