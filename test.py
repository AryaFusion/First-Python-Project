from tvmaze_service import get_shows

data = get_shows()

for show in data[:10]:
    print(show["name"])