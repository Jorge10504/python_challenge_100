from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the silent bid program. Let's get started!")

bidding_active = True
user_bids = {}


def highest_bid(bids_dictionary):
    highest_value = 0
    highest_bidder = ""
    for key in bids_dictionary:
        if bids_dictionary[key] > highest_value:
            highest_value = bids_dictionary[key]
            highest_bidder = key
    print(f"The winner of the auction is {highest_bidder} with a bid of ${highest_value}")


while bidding_active:
    user_name = input("What is your name?\n")
    user_bid = int(input("What is your bid:\n$"))
    user_bids[user_name] = user_bid
    continue_bid = input("Is there another user? Type 'yes' or 'no'\n").lower()
    if continue_bid == "yes":
        print("\n" * 100)
    else:
        bidding_active = False
        highest_bid(user_bids)
