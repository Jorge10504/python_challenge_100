import random

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
    """Returns a random card from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Returns the total sum of the list provided as an input"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare (u_score, c_score):
    if c_score == u_score:
        return "It's a Draw!"
    elif c_score == 0:
        return "You lose. The computer has a blackjack!"
    elif u_score == 0:
        return "Congratulations. You win with a blackjack!"
    elif u_score > 21:
        return "You went over 21, you lose."
    elif c_score > 21:
        return "The computer has gone over 21. You win!"
    elif u_score > c_score:
        return "Congratulations. You win closest to 21!"
    else:
        return "You lose furthest from 21."


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(user_cards)
        print(f"Your cards are: {user_cards}, current score: {user_score}.")
        print(f"The computer's first card is: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or computer_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards}, final score: {user_score}")
    print(f"The computer's final hand is: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Would you like to play a game of blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
