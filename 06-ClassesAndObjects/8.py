class University():

    def __init__(self):
        self.name = 'UEK'    

    def print_name(self):  
        print(self.name)
        
    def set_name(self, new_name):
        self.name = new_name


zmienna = University()

zmienna.print_name()
zmienna.set_name("AGH")
zmienna.print_name()
