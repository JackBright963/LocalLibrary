#This file is like the 'main menu' for your library. Each script you
#write will contain functions, and those scripts are imported here:

import validate
import bookcheckout
import bookweed
import booksearch
import bookreturn

while True:
  #This will loop forever unless a user chooses option 5 to quit
  #Ideally this will be replaced with a nice graphical user interface
  print('\nLibrary menu:')
  print('1 Search')
  print('2 Borrow')
  print('3 Return')
  print('4 Weed')
  print('5 Quit')
  choice=validate.input_int('Yor choice: ')
  if choice == 1:
    booksearch.Book_Search()
  if choice==2:
    bookcheckout.Book_Checkout()
  if choice == 3: 
    bookreturn.book_return()
  if choice==4:
    bookweed.do_weed()
  if choice==5:
    print('Thank you for visiting the library.')
    exit()
    
