# Two modules are imported:
# datetime - so that comparisons between dates can be made
# validate - to ensure the user enters an integer number of days

import validate
import datetime

def Book_Checkout():
 
# This part of the code asks for an ID of a user and book, and makes sure that user's ID is of acceptable lenght

  Student_ID = str(validate.input_int('Please enter your 4-digit student ID: '))
  if len(Student_ID) < 4 or len(Student_ID) > 4 :
    print ('Only 4 numbers allowed!')
  Book_ID = str(validate.input_int('Please enter the ID of a book you wish to checkout: '))


  bookfile = open('database.txt', 'r')
  book_list = bookfile.readlines()
  bookfile.close()
  found = False
  index = 0
  while index < len(book_list) :
    Book_Details = book_list[index].split('|')
    if Book_Details[0] == Book_ID :
      found = True
      if Book_Details[3] != '0':
        print ('This book has been taken from the library by student', Book_Details[3])
        return False
      else:
        Book_Details[3] = Student_ID
        str1 = '|'.join(Book_Details)
        #print(str1)
        book_list[index] = str1
    index = index + 1


# This part is about changing the textfiles, so there is a record of a book being taken

  if found == False :
    print('That book does not exist')
  else:
    #print(book_list)
    bookfile = open('database.txt', 'w')
    bookfile.writelines(book_list)
    bookfile.close()
    logfile = open('logfile.txt', 'a')
    today=datetime.datetime.now()
    change = Book_ID + '|' + today.strftime('%Y-%m-%d') + '|' + 'Borrowed' + '|\n'
    #print (change) 
    logfile.write(change)
    logfile.close()
    print ('Checkout successful')
