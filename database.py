import sqlite3

DB_NAME = "shows.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS searches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        show_name TEXT NOT NULL,
        search_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_search(show_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO searches (show_name) VALUES (?)",
        (show_name,)
    )

    conn.commit()
    conn.close()


def get_recent_searches(limit=5):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT show_name, search_time
    FROM searches
    ORDER BY search_time DESC
    LIMIT ?
    """, (limit,))

    data = cursor.fetchall()

    conn.close()

    return data


if __name__ == "__main__":
    create_database()

    # Testing
    save_search("Dark")
    save_search("Wednesday")

    print("Recent Searches:")
    for search in get_recent_searches():
        print(search)