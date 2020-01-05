class TV():
    def __init__(self):
        self.is_on = 0
        self.channel_no = 1
    
    def on(self):
        self.is_on = 1
    
    def off(self):
        self.is_on = 0
        
    def show_status(self):
        if self.is_on == 0:
            print('Telewizor jest wyłączony')
        else:
            print(f'Telewizor jest załączony, kanał {self.channel_no}')

zmienna = TV()
zmienna.show_status()
zmienna.on()
zmienna.show_status()
zmienna.off()
zmienna.show_status()
