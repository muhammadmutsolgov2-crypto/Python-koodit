import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost", database="flight_game", user="root", password="1234"
)

kursori = yhteys.cursor()

icao_koodi = input("Anna lentoaseman ICAO-koodi (esim. EFHK): ").strip().upper()

sql = "SELECT name, municipality FROM airport WHERE ident = %s"
kursori.execute(sql, (icao_koodi,))
tulos = kursori.fetchone()

if tulos:
  nimi, sijainti = tulos
  print(f"Lentokenttä: {nimi}")
  print(f"Sijaintikunta: {sijainti}")
else:
  print(
      f"Antamallasi ICAO-koodilla '{icao_koodi}' ei löytynyt lentokenttää."
  )

kursori.close()
yhteys.close()