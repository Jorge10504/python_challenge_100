import random

logo = """
  _   _                 _                  ____                     
 | \ | |_   _ _ __ ___ | |__   ___ _ __   / ___|_   _  ___  ___ ___ 
 |  \| | | | | '_ ` _ \| '_ \ / _ \ '__| | |  _| | | |/ _ \/ __/ __|
 | |\  | |_| | | | | | | |_) |  __/ |    | |_| | |_| |  __/\__ \__ \
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \____|\__,_|\___||___/___/
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

random_number = random.choice(numbers)

def hard_mode():
  lives = 5
  
  print("You have 5 attempts to guess the number")
  user_guess = int(input("Make a guess: "))
  
  while lives > 0:
    if user_guess == random_number:
      print(f"You guessed it! The number was {random_number}")
      break
    elif user_guess > random_number:
      print("Too high.")
      lives -= 1
      print(f"You have {lives} live(s) left")
    elif user_guess < random_number:
      print("Too low.")
      lives -= 1
      print(f"You have {lives} live(s) left")
    
    user_guess = int(input("Make another guess: "))
    
    if lives <= 0:
      print(f"You lost, the correct number was: {random_number}")

def easy_mode():
  lives = 10
  
  print("You have 10 attempts to guess the number")
  user_guess = int(input("Make a guess: "))
  
  while lives > 0:
    if user_guess == random_number:
      print(f"You guessed it! The number was {random_number}")
      break
    elif user_guess > random_number:
      print("Too high.")
      lives -= 1
      print(f"You have {lives} live(s) left")
    elif user_guess < random_number:
      print("Too low.")
      lives -= 1
      print(f"You have {lives} live(s) left")
    user_guess = int(input("Make another guess: "))
    
    if lives <= 0:
      print(f"You lost, the correct number was: {random_number}")
    
print(logo)
print("Welcome to the guessing number game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
print(f"Psst, the correct number is {random_number}")
    
if difficulty == "easy":
  easy_mode()
elif difficulty == "hard":
  hard_mode()
