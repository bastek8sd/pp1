class University():

    def __init__(self):
        self.name = 'UEK'
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'
   
    def print_fullname(self):
        print(self.fullname)
        
    def set_fullname(self):
        self.fullname = 'Inna nazwa Uczelni'


zmienna = University()

zmienna.print_fullname()
zmienna.set_fullname()
zmienna.print_fullname()


