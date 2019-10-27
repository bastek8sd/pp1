tab = [12, 6, 4, 9, 3]
for x in tab:
	licznik = ''
	for y in range(x):
		licznik += '*'
	print(str(x) + ": " + licznik + "\n")