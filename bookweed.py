#This module creates three functions:
# activelist(int max_age) searches the logfile for a list of books that have been in active use within the past max_age days
# do_weed() asks the user for the number of days; calls activelist to retrieve a list of active books; then searches the
# database to list to the user all of the books NOT in the activelist, proposing them for deletion
# delete_books() that is sent a list of books ready for deleting

# Two modules are imported:
# datetime - so that comparisons between dates can be made
# validate - to ensure the user enters an integer number of days

import datetime
import validate

def do_weed():
  # This function first asks for input, then calls activelist() to find all active books
  # It then opens the database to form a list of all the other books (ie the inactive ones)
  # Two lists are formed: all inactive books; and all inactive not-on-loan books
  # The option is then given to delete books in either list; or no books
  days=0
  while days<=0:
    days=validate.input_int('Enter activity period, in days: ')
  # call the activelist function to get a set of acitve book_id's
  activebooks=activelist(days)

  print('\nThe following books have not been active within the past',days,'days:')

  all_inactive=[]
  notloan_inactive=[]

  bookfile = open("database.txt","r")
  book_list = bookfile.readlines()
  bookfile.close()
  for book in book_list:
    book_details=book.split("|")
    book_id=book_details[0]
    book_title=book_details[1]
    book_author=book_details[2]
    book_borrower=book_details[3]
    if book_id not in activebooks:
      all_inactive.append(book_id)
      tabs='\t\t'
      if int(book_id)>99 :
        tabs='\t'
      if book_borrower=='0':
        notloan_inactive.append(book_id)
        print('ID:',book_id,tabs,'Title:',book_title)
      else:
        print('ID:',book_id,tabs,'Title:',book_title,'\t\tCurrently on loan to:',book_borrower)
  #print(all_inactive)
  #print(notloan_inactive)
  if len(all_inactive)==0:
      print("No inactive books found.")
      return True
  if (len(all_inactive)==len(notloan_inactive)):
    print ('\nPlease select one of the following options:')
    print ('0  Do not delete any books')
    print ('1  Delete all',len(notloan_inactive),'inactive books')
    while True:
      choice=validate.input_int('Your choice: ')
      if choice==0:
        return True
      if choice==1:
        delete_books(notloan_inactive)
        return True  
  # We're at this stage if the two lists are different
  print ('\nPlease select one of the following options:')
  print ('0  Do not delete any books')
  print ('1  Delete all',len(notloan_inactive),'inactive books not currently on loan')
  print ('2  Delete all',len(all_inactive),'inactive books, including those on loan')
  while True:
    choice=validate.input_int('Your choice: ')
    if choice==0:
      return True
    if choice==1:
      delete_books(notloan_inactive)
      return True
    if choice==2:
      delete_books(all_inactive)
      return True
  return True



def activelist(max_age):
  # Searches through the logfile and returns a set of all book_id's that have been 'active' up to max_age days ago
  # Books could be deleted from the database if they DON'T appear in this list
  
  today=datetime.datetime.now()
  #print(today)

  #define an empty set that will have active book_id's added (set is preferable to list as it will avoid duplication)
  #this list will be returned by the function
  hitlist=set()

  logfile = open("logfile.txt","r")
  log_list=logfile.readlines()
  logfile.close()
  for log_entry in log_list:
    log_item = log_entry.split("|")
    # log_item is a list of 3 strings: 0=book_id; 1=date; 2=action
    log_bookid= log_item[0]
    log_date = datetime.datetime.strptime(log_item[1], '%Y-%m-%d')
    log_action= log_item[2]

    age=(today - log_date).days
    #print(log_bookid,age,log_action)
    if age<=max_age:
      if log_action != 'Deleted':
        #No need to include deleted books in the hitlist
        hitlist.add(log_bookid) 
  
  return hitlist

def delete_books(deletelist):
  #This function opens the database, creates a booklist and then removes from that list all books with id's listed in
  #deletelist. Finally it rewrites the database with the remaining books.
  #print (deletelist)
  print(len(deletelist),'books deleted. * THIS FUNCTION NOT ACTUALLY PROGRAMMED YET :) *')
  return True


