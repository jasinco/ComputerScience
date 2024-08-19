from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="../frontend/dist"), "static")

@app.get("/")
async def root_proxy():
    return RedirectResponse("/static/index.html")
