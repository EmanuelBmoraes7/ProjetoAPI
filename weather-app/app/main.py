from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.weather import Weather, get_weather

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request, city: str = "Palmas"):
    weather = get_weather(city)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "weather": weather},
    )


@app.get("/api/weather", response_model=Weather)
def api_weather(city: str = "Palmas"):
    return get_weather(city)
