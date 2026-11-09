from flask import Flask, jsonify

app = Flask(__name__)
app.json.sort_keys = False


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


@app.route("/alkuluku/<int:number>")
def alkuluku(number):
    return jsonify({"Number": number, "isPrime": is_prime(number)})


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)