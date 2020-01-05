class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
    
    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False
    
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
        
    def set_channels(self, channels_list):
        self.channels = channels_list
        
    def show_channels(self):
        print(self.channels)
        
    def show_status(self):
        if self.is_on:
            print(f'Telewizor jest załączony, kanał {self.channel_no}')
        else:
            print('Telewizor jest wyłączony')

zmienna = TV()
zmienna.show_status()
zmienna.on()
zmienna.show_status()
zmienna.show_channels()
zmienna.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox'])
zmienna.show_channels()
zmienna.show_status()
zmienna.off()