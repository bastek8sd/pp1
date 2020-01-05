class Ulamek():
    from math import gcd
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
        self.ulamek = None
    def create(self):
        self.ulamek = str(int(self.licznik)) + '/' + str(int(self.mianownik))
    def skrot(self):
        try:
            self.nwd = self.gcd(self.licznik, self.mianownik)
            self.licznik = self.licznik / self.nwd
            self.mianownik = self.mianownik / self.nwd
            self.create()
        except:
            print('Nie można skrócić ułamka')
    def show(self):
        print(f'Ułamek to: {self.ulamek}')
        
zmienna = Ulamek(18,4)
zmienna.show()
zmienna.create()
zmienna.show()
zmienna.skrot()
zmienna.show()