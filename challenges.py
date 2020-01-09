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


""" Coding Challenge 4 """

def Counter(incrementer, max):
  max += incrementer
  for num in range(0,max,incrementer):
    print(num)
Counter(2,10)



def Largest_Number(array):
  array.sort()
  print(f"Largest Number is {array[-1]}")
Largest_Number([1,2,7,4,5])

""" Coding Challenge 5 """

word = "word"
sentence = "The cow jumped over the moon"

def word_reverse(word):
  word = word[::-1]
  print(word)
word_reverse(word)

def reverse_sentence(sentence): 
  sentence = sentence[::-1] 
  print(sentence)
reverse_sentence(sentence)


""" Coding Challenge 6 """

import random

list = ['a', 'b', 'c', 'd', 'e', 'f','0','1','2','3','4','5','6','7','8','9']

def random_hex(list):
  hex_list = random.choices(list, k=6)
  join_list = ''.join(hex_list)
  new_hex = '#' + join_list
  print(new_hex)

random_hex(list)


string = "I like turtles"

def frame(string):
  new_string = string.split()
  for i in new_string:
    print('#',i,'#')
frame(string)

""" Coding Challenge 7 """

def even_odd(num):
  if num % 2 == 0:
    print("The number is even...")
  else:
    print("The number is odd...")
even_odd(5)



def popper():
  container = []
  num = 654317
  for i in map(int,str(num)):
    if i <= 5:
      container.append("1")
    elif i > 5:
      container.append("0")
    else:
      print("Bad")
  print("".join(container))
popper()

""" Coding Challenge 8 """

import random
def guessing_game():
  min = 0
  max = 101
  answer = random.randint(min, max)
  guess = input("What is your Guess? ")
  if guess.isalpha():
    print("Thats an Invalid Choice\n")
    guessing_game()
  else:
    guess = int(guess)
    while answer != "guess":
      if guess < answer and guess < max:
        print("Guess a little higher\n")
        guess = int(input("What is your Guess? "))
      elif guess > answer and guess < max:
        print("Guess a little lower\n")
        guess = int(input("What is your Guess? "))
      elif  guess > max:
        print("Invalid Answer...Try Again\n")
        guess = int(input("What is your Guess? "))
      elif guess == answer:
        print("You've guessed correctly...Good Job")
        break
      
guessing_game()

""" Coding Challenge 9 """

def palindrome(word):
  if word == word[::-1]:
    print("Its a palindrome")
  else:
    print("Its not a palindrome")
palindrome('racecar')

""" Coding challenge 10 """

def fizzbuzz(max_num):
  for num in range(max_num + 1):
    if num % 3 == 0 and num % 5 == 0:
      print("fizzbuzz")
    elif num % 5 == 0:
      print("buzz")
    elif  num % 3 == 0:
      print("fizz")
    else:
      print(num)
fizzbuzz(100)

""" Coding Challenge 11 """
# Pig Latin translator

def translator():
    string = ("Jonny Boy").split()
    for word in string:
        print(word[1:] + word[0] + "ay", end = " ")
        # Add (, end = " ") to keep same line
translator()

""" Coding Challenge 12 """

def zipper():
  first_array = [1,2,3]
  second_array = [4,5,6]
  zipped = zip(first_array, second_array)
  # "".join(zipped)
  array = [*zipped]
  print("".join(str(array)))
  
zipper()

""" Diner in Python """

def diner():
  main_menu = {
    "pizza": ["Pizza", 2],
    "tacos": ["Tacos", 2.50]
  }

  side_menu = {
    "fries": ["Fries", 1],
    "tatertots": ["Tatertots", 1.50]
  }

  bill = 0

  # Display the menus
  # Choose from the menus
  # Total their bill

  def greeting():
    print("Welcome to the Python Diner!")

  def menu_display(menu):
    for item in menu.values():
      print(f"{item[0]} => ${item[1]}")

  def user_selection(menu):
    while True:
      user_input = input("\nWhat item would you like? ").lower()
      menu_selection = menu.get(user_input, False)
      if menu_selection == False:
        print("I'm sorry, but that was not on the menu...")
        continue
      else:
        print(f"You picked {menu_selection[0]}, great choice!")
        return menu_selection[1]

  def checkout():
    print(f"\nYour bill today will be ${bill:.2f}")
    print("\nThank you for dining at the Python Diner! Have a great day!")

  greeting()

  print("\nHere is the main menu:")
  menu_display(main_menu)

  bill += user_selection(main_menu)

  print("\nHere is the side menu:")
  menu_display(side_menu)

  bill += user_selection(side_menu)

  print("\nWhat would you like for your second side?")
  menu_display(side_menu)

  bill += user_selection(side_menu)

  checkout()

diner()

""" Dunder Methods """

class Career:
  def __init__(self, name, job):
    self.name = name
    self.job = job

  def __str__(self):
  return f"Job offer to {self.name} who is interested in {self.job}"

  def __repr__(self):
  return f"Job Offer for {self.name}, {self.job}"

  def Static_Method():
    return f"This is pointless"


job = Career('Jonny', 'Full Stack Dev')
print(str(job))
print(repr(job))
print(Career.Static_Method())

""" CodeWars Challenge """

def get_sum(a,b):
  if a == b:
    print(b)
  else:
    sum = 0
    c = b + 1
    for i in range(a,c):
      sum += i
      print(sum)
get_sum(0,4)

""" Challenge """

def remove_smallest(numbers):
  array = numbers[:]
  if array:
    array.remove(min(array))
  print(array)
remove_smallest([3,5,2,5,7,1])