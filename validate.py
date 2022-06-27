# This module just contains one function that is used to ensure the user
#types in an integer value. It is used in the program instead of just input()

def input_int(text):
  while True:
    value = input(text)

    try:
      return int(value)
    except ValueError:
      print(value,'is not a valid number')
