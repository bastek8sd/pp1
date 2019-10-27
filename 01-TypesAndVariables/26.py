# BMI
def calc_bmi(waga,wzrost):
    bmi =  waga/(wzrost/100)**2
    if bmi < 18.5:
        return bmi,'niedowaga'
    elif bmi >= 18.5 and bmi < 25:
        return bmi,'waga prawidłowa'
    elif bmi >=25 and bmi < 30:
        return bmi,'nadwaga'
    else:
        return bmi,'otyłość'
wzrost = float(input('Podaj wzrost w cm: '))
waga = float(input('Podaj wagę w kg: '))

print('Wskaźnik BMI: {0} ({1})'.format(calc_bmi(waga,wzrost)[0],calc_bmi(waga,wzrost)[1]))
