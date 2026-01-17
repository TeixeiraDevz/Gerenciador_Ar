# 🔍 Como Verificar Logs do Vercel para Erro 500

## 📋 Passos para Ver os Logs

### 1. Via Dashboard do Vercel

1. **Acesse:** https://vercel.com/dashboard
2. **Clique** no seu projeto `gerenciador-ar`
3. **Vá em:** Deployments
4. **Clique** no último deploy (o mais recente)
5. **Clique em:** Functions → `api/index.py`
6. **Veja:** Runtime Logs ou Logs

### 2. Via CLI (se preferir)

```powershell
# Ver logs em tempo real
vercel logs --follow

# Ou ver logs de um deploy específico
vercel logs [deployment-url]
```

---

## 🔍 O que Procurar nos Logs

Procure por erros como:

- ❌ `ModuleNotFoundError` - Módulo não encontrado
- ❌ `FileNotFoundError` - Arquivo não encontrado  
- ❌ `sqlite3.OperationalError` - Erro no SQLite
- ❌ `ImportError` - Erro de importação
- ❌ `AttributeError` - Erro de atributo

---

## 💡 Problemas Comuns e Soluções

### Problema 1: SQLite não funciona no Vercel Serverless

**Erro típico:** `sqlite3.OperationalError` ou `readonly database`

**Por quê:** SQLite precisa de sistema de arquivos persistente, mas serverless é stateless.

**Solução:** Use um banco externo (PostgreSQL, MySQL, etc.)

### Problema 2: Módulos não encontrados

**Erro típico:** `ModuleNotFoundError: No module named 'X'`

**Solução:** Verifique se `requirements.txt` tem todas as dependências

### Problema 3: Caminhos de arquivos

**Erro típico:** `FileNotFoundError` ou `TemplateNotFound`

**Solução:** Já configurado em `app.py` com caminhos absolutos

---

## 🔧 Solução Rápida: Desabilitar SQLite Temporariamente

Para testar se o problema é o SQLite, podemos fazer a app funcionar sem banco:

### Opção 1: Modificar init_db para não quebrar

Já está configurado em `app.py` com `try/except`, então se SQLite falhar, a app ainda inicia.

### Opção 2: Usar dados mockados (temporário)

Criar uma versão que funciona sem banco para teste.

---

## 📊 Próximos Passos

1. ✅ Verifique os logs seguindo os passos acima
2. ✅ Copie a mensagem de erro completa dos logs
3. ✅ Compartilhe o erro específico que aparecer
4. ✅ Com o erro específico, posso dar a solução exata

---

**Depois de ver os logs, me envie a mensagem de erro que aparecer!** 🚀
