def losuj():
    from random import randint
    return randint(1, 50)

nums = []
niep = 0
parz = 0

for i in range(1000):
    num = losuj()
    nums.append(num)
    if num % 2 == 0:
        parz += 1
    else:
        niep += 1

print('\
    Dla 1000 liczb losowych z przedziału <1,50>:\n\
    Liczby parzyste: {:.2f}%\n\
    Liczby nieparzyste: {: .2f} %'.format(parz/1000*100, niep/1000*100))