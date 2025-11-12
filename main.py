from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

# Разрешаем CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate_design(
    image: UploadFile = File(...),
    room: str = Form("bedroom"),
    theme: str = Form("modern")
):
    # Отправляем запрос к RoomGPT API
    url = "https://api.roomgpt.io/api/v1/rooms"
    files = {"image": (image.filename, await image.read(), image.content_type)}
    data = {"room": room, "theme": theme}

    try:
        r = requests.post(url, data=data, files=files, timeout=60)
        return JSONResponse(content=r.json())
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
