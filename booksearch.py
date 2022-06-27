def Book_Search():
  Book_Title = input('Please enter the book title: ')

# The following code is to find a book according to the title that is provided by a user.
# Firstly, it will read throught the whole textfile and split the lines in such way
# so they become lists of strings, which makes it easier to find a book based on the title.

  bookfile=open("database.txt","r")
  #print (bookfile.readlines())
  book_list = bookfile.readlines()
  found = False
  for book in book_list :
    book = book.strip()
    Book_Details = book.split('|')
    #print (Book_Details)
    if Book_Details[1] == Book_Title :
      found = True
      print ('Book ID: ', Book_Details[0])
      print ('Book Title: ', Book_Details[1])
      print ('Author: ', Book_Details[2])
      if Book_Details[3] == '0' :
        print ('The book is available in the library \n')
     
      else:
        print ('The book is currently held by student', Book_Details[3], '\n')

  bookfile.close()
  if found == False :
    print ('No matching book found')

