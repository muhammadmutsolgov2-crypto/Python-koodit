

import json
import sys
import urllib.error
import urllib.request

API_URL = "https://api.chucknorris.io/jokes/random"


def hae_vitsi() -> str:
    pyynto = urllib.request.Request(
        API_URL,
        headers={
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (chuck-norris-joke-script)",
        },
    )
    with urllib.request.urlopen(pyynto, timeout=10) as vastaus:
        data = json.load(vastaus)
    return data["value"]


def main() -> int:
    try:
        print(hae_vitsi())
    except (urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError) as virhe:
        print(f"Vitsin haku epäonnistui: {virhe!r}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())