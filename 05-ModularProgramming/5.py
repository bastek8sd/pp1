from statistics import mean, median, stdev

tab = [21600, 4350, 3920, 5590, 3250, 4010]

srednia = mean(tab)
mediana = median(tab)
odchylenie = stdev(tab)

print(f'Średnia arytmetyczna: {srednia}\nMediana: {mediana}\nOdchylenie standardowe: {odchylenie}')