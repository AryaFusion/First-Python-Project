from database import get_recent_searches, get_most_searched

def analytics_report():
    return {
        "most_searched": get_most_searched(),
        "recent_searches": get_recent_searches()
    }