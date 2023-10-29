from random import randint

logo = """
  _   _                 _                  ____                     
 | \ | |_   _ _ __ ___ | |__   ___ _ __   / ___|_   _  ___  ___ ___ 
 |  \| | | | | '_ ` _ \| '_ \ / _ \ '__| | |  _| | | |/ _ \/ __/ __|
 | |\  | |_| | | | | | | |_) |  __/ |    | |_| | |_| |  __/\__ \__ \
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \____|\__,_|\___||___/___/
"""

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  """Checks answer against guess and returns number of turns remaining"""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns -1
  else: 
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
  
def game():
  print(logo)
  print("Welcome to the guessing game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1,100)
  
  print(f"Psst, the answer is {answer}")
  turns = set_difficulty()
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number. ")
    
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    
    if turns == 0:
      print("You've ran out of guesses. You lose!")
      return
    elif guess != answer:
      print("Try again.")

game()
