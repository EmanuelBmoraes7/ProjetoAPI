@echo off
echo ========================================
echo  Iniciando Weather App...
echo ========================================
echo.

echo [1/3] Instalando dependencias...
pip install -r requirements.txt
echo.

echo [2/3] Iniciando servidor FastAPI...
echo.
echo Acesse: http://localhost:8000
echo.
timeout /t 2

uvicorn app.main:app --reload

pause
