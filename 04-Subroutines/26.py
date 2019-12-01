def podatek(dochod):
    if dochod <= 5000:
        return 0.17 * dochod
    else:
        return (5000 * 0.17) + 0.32 * (dochod - 5000)
        
tax = float(input('Podaj dochód: '))
print(f'Podatek należny: {podatek(tax)} zł')
