@echo off
chcp 65001 >nul
echo.
echo ========================================
echo   🌤️  Weather App - Iniciando...
echo ========================================
echo.

REM Verifica se está na pasta correta
if not exist "requirements.txt" (
    echo ❌ ERRO: requirements.txt não encontrado!
    echo.
    echo Certifique-se de que você está na pasta 'weather-app'
    echo.
    pause
    exit /b 1
)

echo ✓ Pasta correta detectada
echo.

echo [1/3] Instalando dependências...
echo.
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Erro ao instalar dependências!
    pause
    exit /b 1
)
echo ✓ Dependências instaladas com sucesso!
echo.

echo [2/3] Iniciando servidor FastAPI...
echo.
echo ========================================
echo   Servidor rodando em:
echo   🌐 http://localhost:8000
echo ========================================
echo.
echo ⏳ Abrindo navegador em 3 segundos...
echo.

timeout /t 3 /nobreak

REM Tenta abrir o navegador
start http://localhost:8000

echo.
echo ✓ Servidor iniciado!
echo.
echo Pressione CTRL+C para parar o servidor
echo.

uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

pause
