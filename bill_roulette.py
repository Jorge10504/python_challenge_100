import random 

names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)

chosen_person = names[random_choice]

print(chosen_person + " is going to buy the meal today!")
