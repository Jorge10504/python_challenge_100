import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

shuffle = False

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
psw_order = input(f"Would you like to shuffle your password? Y/N\n")

# Sequenced Order - Easy Level
new_password = ""

for letter in range(1, nr_letters + 1):
    choice = random.choice(letters)
    new_password += choice

for symbol in range(1, nr_symbols + 1):
    choice = random.choice(symbols)
    new_password += choice

for number in range(1, nr_numbers + 1):
    choice = random.choice(numbers)
    new_password += choice

# Random Order
if psw_order == "Y":
    shuffle = True

if shuffle:
    psw_shuffled = "".join(random.sample(new_password, len(new_password)))

print(f"Your new password is: {new_password}")
