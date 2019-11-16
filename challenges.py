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
  