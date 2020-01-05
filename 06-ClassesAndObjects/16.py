from class_16 import Ebook

book = Ebook('Przykładowy tytuł książki', 'Jakiś autor książki', 200)
book.open()
book.showStatus()
book.next()
book.next()
book.next()
book.showStatus()
book.close()
book.next()