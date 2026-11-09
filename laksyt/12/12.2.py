import requests

API_KEY = "b6af90d60aa079c68347d4e495282764"
URL = "https://api.openweathermap.org/data/2.5/weather"


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def main():
    paikkakunta = input("Anna paikkakunnan nimi: ")
    params = {"q": paikkakunta, "appid": API_KEY, "lang": "fi"}

    try:
        response = requests.get(URL, params=params, timeout=10)
        data = response.json()
    except requests.exceptions.RequestException as e:
        print("Pyyntö epäonnistui:", e)
        return

    if response.status_code != 200:
        print("Virhe:", data.get("message", "tuntematon virhe"))
        return

    kuvaus = data["weather"][0]["description"]
    lampotila = kelvin_to_celsius(data["main"]["temp"])
    print(f"Sää paikkakunnalla {paikkakunta}: {kuvaus}")
    print(f"Lämpötila: {lampotila:.1f} °C")


if __name__ == "__main__":
    main()