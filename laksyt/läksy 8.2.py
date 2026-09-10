import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost", database="flight_game", user="root", password="1234"
)

kursori = yhteys.cursor()

maakoodi = input("Anna maakoodi (esim. FI): ").strip().upper()

sql = (
    "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"
)
kursori.execute(sql, (maakoodi,))
tulokset = kursori.fetchall()

if tulokset:
  print(f"\nLentokentät maassa {maakoodi} tyypeittäin:")
  for kentta_tyyppi, maara in tulokset:
    print(f"- {kentta_tyyppi}: {maara} kappaletta")
else:
  print(f"Maakoodilla '{maakoodi}' ei löytynyt lentokenttiä.")

kursori.close()
yhteys.close()