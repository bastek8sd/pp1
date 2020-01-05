class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    
    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False
    
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no - 1
        
    def set_channels(self, channels_list):
        self.channels = channels_list
        
    def volUp(self):
        if self.volume < 10:
            self.volume += 1
        
    def volDown(self):
        if self.volume > 0:
            self.volume -= 1
        
    def show_channels(self):
        print(self.channels)
        
    def show_status(self):
        if self.channels != []:
            if self.is_on:
                print(f'Telewizor jest załączony, kanał {1 + self.channel_no} ({self.channels[self.channel_no]})\nPoziom głośności: {self.volume}')
            else:
                print('Telewizor jest wyłączony')
        else:
            print('Brak kanałów na liście')

zmienna = TV()
zmienna.on()
zmienna.show_status()
zmienna.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'kanał 6', 'kanał 7'])
zmienna.show_channels()
zmienna.set_channel(4)
zmienna.volUp()
zmienna.show_status()
zmienna.off()

