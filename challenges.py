""" Challenge 1 """

def greeting():
  user_input = input("How are you today? ")
  if user_input.lower() == "good":
    print("That's good I hope you have a splendid day!")
  elif user_input.lower() == "bad":
    print("Your day can only get better then...")
  else:
    print("Hopefully you have a great day")
greeting()


def greeting_two():
  user_input = input("What's your name? ")
  print(f"Good morning {user_input};)")
greeting_two()

""" doesnt work yet """
# good_things = {'good', 'great', 'splendid', 'excellent', 'fantastic', 'perfect'}

# bad_things = {'bad', 'horrible', 'exhausted', 'tired', 'drowsy'}

# good_responses = good_things.values()
# bad_responses = bad_things.values()
# def greeting():
#   user_input = input("How are you today? ")
#   if user_input.lower() == good_responses:
#     print("That is muy bueno, I hope it continues to be the best")
#   elif user_input.lower() == bad_responses:
#     print("I hope your day gets better from here...")
#   else:
#     print("I don't know that answer but have a great day")
# greeting()
  

""" Challenge 2 """

""" If name matches it prints out a specialized message. The next one if its a number then it would add 5 if not it would say that it can't """

def name_classifier():
  user_input = input("What is your name? ")
  if user_input.lower() == "mario":
    print(f"Hello Mario!")
  elif user_input.lower() == "luigi":
    print("Hi Luigi!")
  else:
    print("You are no bueno")
name_classifier()


def number_add(number):
  if number == int(number):
    print(number + 5)
  else:
    print("Not a number")

number_add(10)


""" Coding Challenge 3 """

# list_uno = ["hello", "bye", "happy"]
# list_dos = ["hola", "adios", "bueno"]

# def list_merger(list_one, list_two):
#   new_list = list_one + list_two
#   print(new_list)

# list_merger(list_uno, list_dos)


# def counter(max):
#   for elements in range(max + 1):
#     print(elements)

# counter(5)

def counter():
 counter = 0
 checker = True
 while counter > 0:
   counter = counter + 1
   print(counter)
   if counter == 5:
     checker = False
     return checker
counter()