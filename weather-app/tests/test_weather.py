from app.weather import describe_weather, get_weather


def test_ceu_limpo():
    assert describe_weather(0) == "Céu limpo"


def test_nublado():
    assert describe_weather(2) == "Nublado"


def test_codigo_invalido():
    assert describe_weather(999) == "Desconhecido"


def test_get_weather_retorna_cidade():
    resultado = get_weather("Palmas")
    assert resultado.city == "Palmas"
    assert resultado.temp_c == 32.5
