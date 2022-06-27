# The first module is imported so that the grapical interface could be created
# Rest of imports are other functions that will be linked to buttons


from tkinter import *
import bookcheckout
import bookweed
import booksearch
import bookreturn
    
# Specifies the layout of the window and links other functions to start operating, when a button is clicked.

window = Tk()
window.title ("Menu")
window.geometry ('300x250')
lbl = Label (window, text = "Choose an option:")
lbl.grid (column=0, row=0)
search = Button (window, text = 'Search for books', command = booksearch.Book_Search)
checkout = Button (window, text = 'Checkout books', command = bookcheckout.Book_Checkout)
returN = Button (window, text = 'Return books', command = bookreturn.book_return)
weed = Button (window, text = 'Weed books', command = bookweed.do_weed)
quiT = Button (window, text = 'Quit library', command = window.destroy)
search.grid (column =  3, row = 1)
checkout.grid (column = 3, row = 2)
returN.grid (column = 3, row = 3)
weed.grid (column = 3, row = 4)
quiT.grid (column = 3, row = 5)
window.mainloop()
