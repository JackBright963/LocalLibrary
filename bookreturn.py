# Two modules are imported:
# datetime - so that comparisons between dates can be made
# validate - to ensure the user enters an integer number of days


import validate
import datetime

# This funtion works in the same way as the one for checking out books.
# The only difference is that it only asks for a book ID and updates
# the text files when a book is returned.

def book_return():

  
  Book_ID = str(validate.input_int('Please enter the ID of a book you wish to return: '))

  bookfile = open('database.txt', 'r')
  book_list = bookfile.readlines()
  bookfile.close()
  found = False
  index = 0
  while index < len(book_list) :
    Book_Details = book_list[index].split('|')
    if Book_Details[0] == Book_ID :
      found = True
      if Book_Details[3] == '0':
        print ('This book has not been taken from the library')
        return False
      else:
        Book_Details[3] = '0'
        str1 = '|'.join(Book_Details)
        #print(str1)
        book_list[index] = str1
    index = index + 1


  if found == False :
    print('That book does not exist')
  else:
   # print(book_list)
    bookfile = open('database.txt', 'w')
    bookfile.writelines(book_list)
    bookfile.close()
    logfile = open('logfile.txt', 'a')
    today=datetime.datetime.now()
    change = Book_ID + '|' + today.strftime('%Y-%m-%d') + '|' + 'Returned' + '|\n'
    #print (change) 
    logfile.write(change)
    logfile.close()
    print ('Return successful')
