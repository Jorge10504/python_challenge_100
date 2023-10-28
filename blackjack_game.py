import random
from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
  """This function returns a random card from the cards list"""""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """This function takes a list of cards and returns the score of the hand"""""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)

def compare(u_score, d_score):
  """This function takes in the value of the user score and dealer score and compares them"""
  if u_score == d_score:
    return "It's a draw!"
  elif d_score == 0:
    return "You lose! Dealer wins with blackjack"
  elif u_score == 0:
    return "You win with a blackjack!"
  elif u_score > 21:
    return "You went over 21. You lose, dealer wins."
  elif d_score > 21:
    return "Dealer went over 21. You win, dealer lost."
  elif u_score > d_score:
    return "You win!"
  else:
    return "You lose!"

def play_game():
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"The dealer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' to start or 'n' to exit.") == "y":
  clear()
  play_game()
