import requests

def get_shows():
    url = "https://api.tvmaze.com/shows"
    response = requests.get(url, timeout=8)

    if response.status_code == 200:
        return response.json()

    return []