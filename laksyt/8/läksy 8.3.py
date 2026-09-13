import mysql.connector
from geopy.distance import great_circle

yhteys = mysql.connector.connect(
    host="localhost", database="flight_game", user="root", password="1234"
)

kursori = yhteys.cursor()

icao1 = (
    input("Anna ensimmäisen lentoaseman ICAO-koodi (esim. EFHK): ")
    .strip()
    .upper()
)
icao2 = (
    input("Anna toisen lentoaseman ICAO-koodi (esim. KJFK): ").strip().upper()
)


def hae_koordinaatit(icao):
  sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
  kursori.execute(sql, (icao,))
  return kursori.fetchone()


koord1 = hae_koordinaatit(icao1)
koord2 = hae_koordinaatit(icao2)

if koord1 and koord2:
  etaisyys = great_circle(koord1, koord2).kilometers
  print(
      f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on"
      f" {etaisyys:.2f} kilometriä."
  )
else:
  print("Toista tai molempia ICAO-koodeja ei löytynyt tietokannasta.")

kursori.close()
yhteys.close()