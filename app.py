from fastapi import FastAPI
from tvmaze_service import get_shows

app = FastAPI()

@app.get("/")
def home():
    return {"message": "OTT Trend Tracker"}

@app.get("/trending")
def trending():
    data = get_shows()
    shows = []

    for show in data[:20]:
        shows.append({
            "name": show["name"],
            "rating": show["rating"]["average"],
            "genres": show["genres"],
            "image": show["image"]["medium"] if show["image"] else None
        })

    return shows

@app.get("/search/{show_name}")
def search_show(show_name: str):
    data = get_shows()
    results = []

    for show in data:
        if show_name.lower() in show["name"].lower():
            results.append({
                "name": show["name"],
                "rating": show["rating"]["average"],
                "genres": show["genres"]
            })

    return results
