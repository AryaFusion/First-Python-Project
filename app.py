from flask import Flask, request, jsonify
from database import init_db, save_search, get_recent_searches, get_most_searched

app = Flask(__name__)
init_db()

@app.route("/search", methods=["POST"])
def search_show():
    data = request.json
    show_name = data.get("show_name")

    if not show_name:
        return jsonify({"error": "show_name required"}), 400

    save_search(show_name)
    return jsonify({"message": f"{show_name} saved successfully"})


@app.route("/analytics/most-searched", methods=["GET"])
def most_searched():
    return jsonify(get_most_searched())


@app.route("/analytics/recent-searches", methods=["GET"])
def recent_searches():
    return jsonify(get_recent_searches())


if __name__ == "__main__":
    app.run(debug=True)