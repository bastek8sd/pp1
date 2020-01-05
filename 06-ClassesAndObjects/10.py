class TV():
    def __init__(self):
        self.is_on = 0
    
    def on(self):
        self.is_on = 1
    
    def off(self):
        self.is_on = 0
        
    def show_status(self):
        if self.is_on == 0:
            print('Telewizor jest wyłączony')
        else:
            print('Telewizor jest załączony')

zmienna = TV()
zmienna.show_status()
zmienna.on()
zmienna.show_status()
zmienna.off()
zmienna.show_status()