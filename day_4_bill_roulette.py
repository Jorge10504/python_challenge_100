import random

print("Welcome to the bill roulette!")
friends_input_list = input("Insert the names of your friends separated by a space.\n")
friends_list = friends_input_list.split()

friends_number = len(friends_list)
random_choice = random.randint(0, friends_number -1)
chosen_person = friends_list[random_choice]

print(f"Congratulations!\n{chosen_person} is going to pay for everyone's meal today.")
