class Ebook():
    def __init__(self, title, author, pages):
        self.status = False
        self.title = title
        self.author = author
        self.pages = pages
        self.page = 1
        
    def open(self):
        if self.status == False:
            self.status = True
    
    def close(self):
        if self.status:
            self.status = False
            
    def back(self):
        if self.page > 1:
            self.page -= 1
        else:
            print('Jesteś na pierwszej stronie')
        
    def next(self):
        if self.status:
            if self.page < self.pages:
                self.page += 1
            else:
                print('Jesteś na ostatniej stronie')
        else:
            self.showStatus()
            self.showStatus()
       
    def showStatus(self):
        if self.status:
            print(f'Książka "{self.title}", autora {self.author} jest otwarta na stronie {self.page} na {self.pages}')
        else:
            print('Książka jest zamknięta.')
