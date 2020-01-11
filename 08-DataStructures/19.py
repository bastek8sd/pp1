#NBP – 10 ostatnich notowań EURO
#Data Kupno Sprzedaż 
#================================ 
#2019-10-25  3.8150  3.9820 
#...         ...     ...


import json


with open("euro.json") as file: 
    data = json.load(file) 
    print('NBP – 10 ostatnich notowań EURO\n\n{:<10}   {:<6}   {:<6}\n{}'.format('Data','Kupno','Sprzedaż','='*32))
    for e in data['rates']: 
        print('{:<10}   {:<6}   {:<6}'.format(e['effectiveDate'], e['bid'], e['ask']))