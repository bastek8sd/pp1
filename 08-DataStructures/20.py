#W języku Python utwórz słownik opisujący komputer zawierający co najmniej 5 par klucz-wartość (każda wartość innego typu). 
#Następnie napisz program, który zapisze dane do pliku komputer.json. 
#Zwróć uwagę na formatowanie danych w pliku json. Zastosuj parametr ‘indent’ w metodzie dump().

komputer = {
    'włączony': True,
    'IlośćRAM': 8,
    'marka': 'Asus',
    'ekran_cale': 15.6,
    'linia_numeryczna': [1,2,3,4,5,6,7,8,9,0]
    }
import json

with open('komputer.json', 'w') as file:
    json.dump(komputer, file, indent=4)
