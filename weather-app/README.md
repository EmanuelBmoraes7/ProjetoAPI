# Weather App

API de previsão do tempo feita com FastAPI.

## Endpoints

- `GET /` — página HTML com a previsão
- `GET /api/weather?city=Palmas` — previsão em JSON

## Como rodar

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Acesse http://localhost:8000

## Testes

```
pytest
```
