from pydantic import BaseModel


# Modelo Pydantic: define o formato da resposta
class Weather(BaseModel):
    city: str
    temp_c: float
    condition: str


def describe_weather(code: int) -> str:
    """Transforma um código numérico em descrição do tempo."""
    if code == 0:
        return "Céu limpo"
    elif code == 1:
        return "Parcialmente nublado"
    elif code == 2:
        return "Nublado"
    else:
        return "Desconhecido"


def get_weather(city: str) -> Weather:
    """Monta a previsão do tempo de uma cidade."""
    return Weather(
        city=city,
        temp_c=32.5,
        condition=describe_weather(1),
    )
