from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests
import re

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def clean_summary(summary):
    if not summary:
        return "No description available."
    return re.sub("<.*?>", "", summary)


def format_show(show):
    name = show.get("name", "Unknown")

    if name == "La Casa de Papel":
        name = "Money Heist"

    return {
        "name": name,
        "type": show.get("type", "TV Show"),
        "language": show.get("language", "Unknown"),
        "status": show.get("status", "Unknown"),
        "premiered": show.get("premiered", "Unknown"),
        "rating": show.get("rating", {}).get("average") or "N/A",
        "genres": show.get("genres", []),
        "summary": clean_summary(show.get("summary")),
        "image": show.get("image", {}).get("medium") if show.get("image") else None,
        "original_image": show.get("image", {}).get("original") if show.get("image") else None
    }


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/trending")
def trending():
    names = [
        "La Casa de Papel",
        "Dark",
        "Stranger Things",
        "Breaking Bad",
        "Peaky Blinders",
        "The Boys",
        "Wednesday",
        "Squid Game",
        "Game of Thrones",
        "House of the Dragon",
        "The Last of Us",
        "The Witcher",
        "Narcos",
        "Loki",
        "The Mandalorian",
        "Alice in Borderland",
        "You",
        "The Office",
        "Arrow",
        "Sherlock"
    ]

    shows = []

    for name in names:
        try:
            url = f"https://api.tvmaze.com/singlesearch/shows?q={name}"
            response = requests.get(url, timeout=8)

            if response.status_code == 200:
                shows.append(format_show(response.json()))
        except Exception:
            continue

    return shows


@app.get("/search/{show_name}")
def search_show(show_name: str):
    try:
        url = f"https://api.tvmaze.com/search/shows?q={show_name}"
        response = requests.get(url, timeout=8)

        if response.status_code != 200:
            return []

        data = response.json()
        results = []

        for item in data[:20]:
            results.append(format_show(item.get("show", {})))

        return results

    except Exception:
        return []