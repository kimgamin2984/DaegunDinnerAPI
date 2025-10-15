from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = "dinner.db"
app.config['JSON_AS_ASCII'] = False 

def get_menu_by_date(date):
    if not os.path.exists(DB_PATH):
        return None
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT menu FROM dinner WHERE date = ?", (date,))
    row = cur.fetchone()
    conn.close()
    return row[0].split("\n") if row else None

@app.route("/")
def home():
    return jsonify({"message": "Daegun Dinner API is running."})

@app.route("/menu", methods=["GET"])
def get_menu():
    date = request.args.get("date")
    if not date:
        return jsonify({"error": "Missing 'date' parameter"}), 400
    menu = get_menu_by_date(date)
    if menu:
        return jsonify({"date": date, "menu": menu})
    else:
        return jsonify({"error": f"No data found for date {date}"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)