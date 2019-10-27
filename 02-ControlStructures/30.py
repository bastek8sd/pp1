# Karta płatnicza - blokowanie po 3 próbach

pin = '0805'
lock = 0

while lock < 3:
    kod = input("Podaj kod PIN: ")
    if kod != pin:
        lock += 1
        print("Kod PIN niepoprawny.")
    else:
        print("Kod PIN został zaakceptowany.")
        break
if lock == 3:
    print("Karta płatnicza zostaje zablokowana.")