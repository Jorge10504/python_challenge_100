print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to the Treasure Island Game!\nYour mission is to find the treasure.")
choice = input("You are at a cross road. Where do you want to go? Type 'left' or 'right.'")

if choice == "right":
    print("Game Over!")
elif choice == "left":
    choice = input(
        "You have come to a lake. There is an island in the middle of the lake. "
        "Type 'wait' to wait for a boat or 'swim' to swim to the island.\n"
    )
    if choice == "wait":
        print("Game Over!")
    elif choice == "swim":
        choice = input(
            "You arrive at the island unharmed. "
            "There is a house with three doors. One is red, one yellow and one blue. "
            "Which color do you choose?\n"
        )
        if choice == "red":
            print("Congratulations, you have found the treasure!")
        else:
            print("Incorrect! Game Over.")
