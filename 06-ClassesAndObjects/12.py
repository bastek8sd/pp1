class TV():
    def __init__(self):
        self.is_on = 0
        self.channel_no = 1
    
    def on(self):
        self.is_on = 1
    
    def off(self):
        self.is_on = 0
    
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
        
    def show_status(self):
        if self.is_on == 0:
            print('Telewizor jest wyłączony')
        else:
            print(f'Telewizor jest załączony, kanał {self.channel_no}')

zmienna = TV()
zmienna.show_status()
zmienna.on()
zmienna.show_status()
zmienna.set_channel(6)
zmienna.show_status()

