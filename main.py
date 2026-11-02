from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests
import asyncio

app = FastAPI()

# Mengizinkan Frontend mengakses API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "Backend Active", "service": "XAU/USD Realtime Engine"}

# Endpoint untuk mengecek status berita (News Lockout)
@app.get("/api/news-lockout-status")
def news_lockout():
    # Anda dapat menghubungkan ke API kalender ekonomi di sini
    return {"is_locked": False, "active_event": None}

# Endpoint untuk mengambil data kalender ekonomi
@app.get("/api/economic-calendar")
def economic_calendar():
    return {
        "status": "success",
        "data": [
            {"event": "US Retail Sales & Core PPI", "date": "2026-10-21 19:30:00"},
            {"event": "Unemployment Claims", "date": "2026-10-22 19:30:00"},
            {"event": "Flash Manufacturing & Services PMI", "date": "2026-10-23 20:45:00"}
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
