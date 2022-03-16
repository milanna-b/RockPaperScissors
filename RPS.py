# Rock Paper Scissors

from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
  "tie": "It's a tie, try again!",
  "won": "You win!",
  "lost": "You lost..."
}

def play():
  user_choice = input("Enter ROCK, PAPER, or SCISSORS ")
  user_choice = user_choice.upper()
  com_choice = options[randint(0, 2)]
  decide_winner(user_choice, com_choice)

def decide_winner(user_choice, com_choice):
  print("You selected " + user_choice)
  print("Computer selected " + com_choice)
  if user_choice == com_choice:
    print(message["tie"])
  elif user_choice == options[0] and com_choice == options[2]:
    print(message["won"])
  elif user_choice == options[1] and com_choice == options[0]:
    print(message["won"])
  elif user_choice == options[2] and com_choice == options[1]:
    print(message["won"])
  else:
    print(message["lost"])

play()