from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
app.json.sort_keys = False

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "database": "flight_game",
    "user": "root",
    "password": "1234",
    "autocommit": True,
}


def get_airport(icao):
    connection = mysql.connector.connect(**DB_CONFIG)
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ident, name, municipality FROM airport WHERE ident = %s",
            (icao,),
        )
        return cursor.fetchone()
    finally:
        connection.close()


@app.route("/kenttä/<icao>")
def kentta(icao):
    row = get_airport(icao.upper())
    if row is None:
        return jsonify({"status": 404, "error": "Lentokenttää ei löytynyt"}), 404
    return jsonify({"ICAO": row[0], "Name": row[1], "Municipality": row[2]})


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)