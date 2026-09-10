import mysql.connector


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )
koodi =  input("Anna maakood")
sql= f"select * from country where iso_country = '{koodi}'"
kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
for rivi in tulos:
    print(rivi)