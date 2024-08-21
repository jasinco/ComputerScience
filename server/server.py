from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import sched, time
import fetcher
from multiprocessing import Process

# Pre-Run to fetch the origin data
fetcher.fetcher()

def schedule_runner():
    schedule = sched.scheduler(time.time, time.sleep)
    while 1:
        # 30 seconds per fetch
        schedule.enter(30*60, 1, fetcher.fetcher)
        schedule.run()
Process(target=schedule_runner)


app = FastAPI()
app.mount("/static", StaticFiles(directory="../frontend/dist"), "static")


@app.get("/api/news")
async def get_news():
    print(fetcher.cached_news)
    return fetcher.cached_news

@app.get("/")
async def root_proxy():
    return RedirectResponse("/static/index.html")
