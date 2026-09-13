yritykset = 0

while yritykset < 5:
    tunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    else:
        yritykset += 1

if yritykset == 5:
    print("Pääsy evätty")