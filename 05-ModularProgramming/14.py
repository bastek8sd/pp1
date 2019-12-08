import csv
from statistics import mean, median, stdev

with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    licznik = 0
    ages = []
    for row in reader:
        if licznik == 0:
            print('{:<5}{:<15}{:<15}{:<6}{:<34}'.format(
                    '#', row[0].upper(), row[1].upper(), row[2].upper(), row[3].upper()))
        else:
            print('{:<5}{:<15}{:<15}{:<6}{:<34}'.format(
                    licznik, row[0].upper(), row[1].upper(), row[2].upper(), row[3].upper()))
            ages.append(row[2])
        licznik += 1
        ages = [int(x) for x in ages]
    print(f'\nŚrednia wieku: {mean(ages)}\nMediana wieku: {median(ages)}\nOdchylenie standardowe: {stdev(ages)}') 