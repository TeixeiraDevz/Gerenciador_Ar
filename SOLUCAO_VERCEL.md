# 🔧 Solução: Erro AF_UNIX no Vercel (Windows)

## ❌ Problema

O erro `AttributeError: module 'socket' has no attribute 'AF_UNIX'` ocorre porque:
- O `vercel dev` local no Windows tenta usar recursos Unix que não existem
- `AF_UNIX` só funciona em Linux/macOS, não no Windows

## ✅ Soluções

### Solução 1: Deploy Direto no Vercel (Recomendado)

**Não use `vercel dev` no Windows.** Faça deploy direto:

```powershell
# 1. Login no Vercel
vercel login

# 2. Deploy direto (SEM vercel dev)
vercel --prod

# Ou via Dashboard do Vercel
# Acesse vercel.com → New Project → Import Git Repository
```

**Vantagem:** Funciona perfeitamente no Windows e deploy é feito na nuvem.

---

### Solução 2: Usar Docker/WSL (Para desenvolvimento local)

Se precisar testar localmente:

```powershell
# Opção A: Usar WSL (Windows Subsystem for Linux)
wsl
cd /mnt/c/Users/Andrea/OneDrive/Documentos/Gerenciador\ Ar
vercel dev

# Opção B: Usar Docker
docker run -it -v ${PWD}:/app vercel/cli vercel dev
```

---

### Solução 3: Testar Localmente com Flask Normal

Em vez de usar `vercel dev`, teste com Flask normal:

```powershell
# Testar localmente como Flask normal
python app.py

# Acesse: http://localhost:5000
```

Depois faça deploy direto no Vercel sem testar com `vercel dev`.

---

## 🚀 Deploy Correto no Vercel (Windows)

### Passo 1: Preparar o Código

✅ Os arquivos já estão configurados:
- `vercel.json` ✅
- `api/index.py` ✅
- `requirements.txt` ✅

### Passo 2: Commit e Push

```powershell
.\deploy.ps1

# Ou manualmente:
git add .
git commit -m "Configurar para Vercel"
git push
```

### Passo 3: Deploy no Vercel Dashboard

1. Acesse https://vercel.com
2. Clique em **New Project**
3. Conecte seu repositório GitHub
4. Selecione o repositório `Gerenciador_Ar`
5. Vercel detecta `vercel.json` automaticamente
6. Clique em **Deploy**

**NÃO use `vercel dev` no Windows!** Use o deploy via Dashboard ou `vercel --prod`.

---

## 📋 Configuração Correta

### Estrutura de Arquivos

```
Gerenciador Ar/
├── api/
│   └── index.py          ✅ Entry point para Vercel
├── vercel.json           ✅ Configuração Vercel
├── app.py                ✅ Flask app
├── requirements.txt      ✅ Dependências
└── ...
```

### vercel.json (Já Configurado)

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ]
}
```

---

## ⚠️ Limitações do Vercel Dev no Windows

O `vercel dev` no Windows tem problemas conhecidos:
- ❌ Não suporta `AF_UNIX` (sockets Unix)
- ❌ Pode ter problemas com file watching
- ✅ **Solução:** Use deploy direto ou WSL/Docker

---

## 🎯 Recomendação Final

**Para Windows:**
1. ✅ Desenvolva localmente com `python app.py`
2. ✅ Teste normalmente no `http://localhost:5000`
3. ✅ Faça deploy via Dashboard do Vercel ou `vercel --prod`
4. ❌ **NÃO use `vercel dev` no Windows**

**O deploy em produção funciona perfeitamente!** O problema é só no `vercel dev` local.

---

## 💡 Dica

Se você realmente precisar testar localmente como no Vercel, use:
- **WSL** (Windows Subsystem for Linux)
- **Docker**
- Ou teste diretamente no Vercel após deploy (versão preview)

---

**Resumo:** O erro é apenas no `vercel dev` local no Windows. O deploy em produção funciona normalmente! 🚀
