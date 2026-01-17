param(
    [string]$MensagemCommit = "Atualização do projeto Gerenciador Ar",
    [switch]$SkipPush = $false
)

Write-Host ""
Write-Host "=== Deploy Automatizado - Gerenciador Ar ===" -ForegroundColor Cyan
Write-Host ""

try {
    $gitVersion = git --version 2>&1
    Write-Host "OK Git encontrado: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "ERRO Git nao encontrado! Instale o Git primeiro." -ForegroundColor Red
    exit 1
}

$projetoFiles = @("app.py", "requirements.txt", "Procfile", "src")
$allFilesExist = $true
foreach ($file in $projetoFiles) {
    if (-not (Test-Path $file)) {
        $allFilesExist = $false
        break
    }
}

if (-not $allFilesExist) {
    Write-Host "ERRO Nao estamos na pasta correta do projeto!" -ForegroundColor Red
    exit 1
}

Write-Host "OK Pasta do projeto confirmada" -ForegroundColor Green
Write-Host ""

if (-not (Test-Path ".git")) {
    Write-Host "Git nao esta inicializado. Inicializando..." -ForegroundColor Yellow
    git init
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERRO Erro ao inicializar Git" -ForegroundColor Red
        exit 1
    }
    Write-Host "OK Git inicializado" -ForegroundColor Green
}

Write-Host ""
Write-Host "Verificando arquivos que nao devem ser commitados..." -ForegroundColor Yellow

$problemas = @()

if (Test-Path "gerenciador_ar.db") {
    $status = git status --porcelain "gerenciador_ar.db" 2>&1
    if ($status -match "^[AM]") {
        $problemas += "gerenciador_ar.db esta sendo commitado!"
    }
}

if ($problemas.Count -gt 0) {
    Write-Host ""
    Write-Host "ATENCAO: Arquivos proibidos serao commitados:" -ForegroundColor Red
    foreach ($problema in $problemas) {
        Write-Host "  - $problema" -ForegroundColor Yellow
    }
    Write-Host ""
    $continuar = Read-Host "Deseja continuar mesmo assim? (s/N)"
    if ($continuar -ne "s" -and $continuar -ne "S") {
        Write-Host "Deploy cancelado." -ForegroundColor Yellow
        exit 0
    }
} else {
    Write-Host "OK Nenhum arquivo proibido sera commitado" -ForegroundColor Green
}

Write-Host ""

Write-Host "Status do repositorio Git:" -ForegroundColor Cyan
git status --short

Write-Host ""

$changes = git status --porcelain
$SkipCommit = $false

if ([string]::IsNullOrWhiteSpace($changes)) {
    Write-Host "Nenhuma mudanca para commitar." -ForegroundColor Yellow
    $continuar = Read-Host "Deseja fazer push mesmo assim? (s/N)"
    if ($continuar -ne "s" -and $continuar -ne "S") {
        Write-Host "Deploy cancelado." -ForegroundColor Yellow
        exit 0
    }
    $SkipCommit = $true
} else {
    Write-Host "Arquivos alterados encontrados:" -ForegroundColor Cyan
    git status --short | ForEach-Object { Write-Host "  $_" }
    Write-Host ""
    $confirmar = Read-Host "Deseja fazer commit dessas mudancas? (S/n)"
    
    if ($confirmar -eq "n" -or $confirmar -eq "N") {
        Write-Host "Deploy cancelado." -ForegroundColor Yellow
        exit 0
    }
    
    Write-Host ""
    $mensagemCustom = Read-Host "Mensagem de commit (Enter para usar padrao: '$MensagemCommit')"
    if (-not [string]::IsNullOrWhiteSpace($mensagemCustom)) {
        $MensagemCommit = $mensagemCustom
    }
    
    $SkipCommit = $false
}

Write-Host ""

if (-not $SkipCommit) {
    Write-Host "Adicionando arquivos ao staging..." -ForegroundColor Yellow
    git add .
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERRO Erro ao adicionar arquivos" -ForegroundColor Red
        exit 1
    }
    
    Write-Host "Fazendo commit..." -ForegroundColor Yellow
    git commit -m $MensagemCommit
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERRO Erro ao fazer commit" -ForegroundColor Red
        exit 1
    }
    
    Write-Host "OK Commit realizado: '$MensagemCommit'" -ForegroundColor Green
    Write-Host ""
}

$remote = git remote -v
if ([string]::IsNullOrWhiteSpace($remote)) {
    Write-Host "Nenhum repositorio remoto configurado." -ForegroundColor Yellow
    Write-Host ""
    $adicionarRemote = Read-Host "Deseja adicionar um repositorio remoto agora? (s/N)"
    
    if ($adicionarRemote -eq "s" -or $adicionarRemote -eq "S") {
        $remoteUrl = Read-Host "URL do repositorio remoto (ex: https://github.com/usuario/repo.git)"
        if (-not [string]::IsNullOrWhiteSpace($remoteUrl)) {
            git remote add origin $remoteUrl
            Write-Host "OK Repositorio remoto adicionado" -ForegroundColor Green
            $remote = git remote -v
        } else {
            $SkipPush = $true
        }
    } else {
        $SkipPush = $true
    }
} else {
    Write-Host "OK Repositorio remoto encontrado:" -ForegroundColor Green
    Write-Host $remote
}

Write-Host ""

if (-not $SkipPush) {
    Write-Host "Verificando branch..." -ForegroundColor Yellow
    $currentBranch = git branch --show-current
    
    if ([string]::IsNullOrWhiteSpace($currentBranch)) {
        Write-Host "Criando branch 'main'..." -ForegroundColor Yellow
        git branch -M main
        $currentBranch = "main"
    }
    
    Write-Host "Branch atual: $currentBranch" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Fazendo push para origin/$currentBranch..." -ForegroundColor Yellow
    
    git push -u origin $currentBranch 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        git push 2>&1 | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Host "ATENCAO Erro ao fazer push" -ForegroundColor Yellow
            Write-Host "  Execute manualmente: git push -u origin $currentBranch" -ForegroundColor Yellow
        } else {
            Write-Host "OK Push realizado com sucesso!" -ForegroundColor Green
        }
    } else {
        Write-Host "OK Push realizado com sucesso!" -ForegroundColor Green
    }
} else {
    Write-Host "Push pulado (usando -SkipPush ou sem remote)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=== Deploy Concluido! ===" -ForegroundColor Green
Write-Host ""

if (-not $SkipPush) {
    Write-Host "Proximos passos:" -ForegroundColor Cyan
    Write-Host "1. Faca deploy no Render/Heroku/Railway" -ForegroundColor White
    Write-Host "2. Configure variaveis de ambiente" -ForegroundColor White
    Write-Host "3. Aguarde o deploy" -ForegroundColor White
}

Write-Host ""
