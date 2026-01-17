# 🔧 Solução: Erro 500 no Vercel

## ❌ Erro Atual

```
500: INTERNAL_SERVER_ERROR
Code: FUNCTION_INVOCATION_FAILED
```

## ✅ Correções Aplicadas

Já fiz os seguintes ajustes:

1. **app.py** - Configuração explícita de templates e static files
2. **api/index.py** - Tratamento de erros melhorado
3. **vercel.json** - Rota para arquivos estáticos adicionada

## 🔍 Como Verificar os Logs

### 1. Verificar Logs no Vercel Dashboard

1. Acesse https://vercel.com/dashboard
2. Clique no seu projeto
3. Vá em **Deployments**
4. Clique no último deploy
5. Clique em **Functions** → **api/index.py**
6. Veja os **Logs** ou **Runtime Logs**

Isso mostrará o erro exato.

## 🚨 Problemas Comuns

### Problema 1: SQLite não funciona no Vercel Serverless

**Sintoma:** Erro ao criar/ler banco de dados

**Solução:** SQLite não é adequado para serverless. Use:
- PostgreSQL (Vercel Postgres - recomendado)
- Ou outro banco gerenciado

### Problema 2: Templates/Static não encontrados

**Sintoma:** Erro ao renderizar templates

**Solução:** Já configurado em `app.py`:
```python
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
```

### Problema 3: Imports falhando

**Sintoma:** ModuleNotFoundError

**Solução:** Verifique se `requirements.txt` tem todas as dependências

## 🛠️ Próximos Passos

1. **Fazer commit das correções:**
   ```powershell
   .\deploy.ps1
   ```

2. **Fazer novo deploy no Vercel:**
   - Dashboard do Vercel → Deployments → Redeploy
   - Ou novo commit triggera deploy automático

3. **Verificar logs após o deploy:**
   - Veja os logs no Dashboard
   - Identifique o erro específico

## 📋 Checklist

- [ ] Commit das correções feito
- [ ] Novo deploy realizado
- [ ] Logs verificados
- [ ] Erro específico identificado

## 💡 Dica: Ver Logs em Tempo Real

```powershell
# Instalar Vercel CLI (se não tiver)
npm install -g vercel

# Ver logs em tempo real (precisa estar logado)
vercel logs --follow
```

---

**Se o erro persistir**, verifique os logs e compartilhe a mensagem de erro específica que aparecer.
