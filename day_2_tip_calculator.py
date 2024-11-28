print("Welcome to the tip calculator!")
total_bill = float(input("What is the bill amount?\n"))
tip_choice = input("Would you like to add a tip? Y/N \n")

if tip_choice == "Y":
    tip_percentage = int(input("How much would you like to tip? 10%, 12%, 15%\n"))
    tip_amount = total_bill * tip_percentage / 100
    number_of_people = int(input("How many people are splitting the bill?\n"))
    final_bill = round(total_bill + tip_amount, 2)
    individual_bill = round(final_bill / number_of_people, 2)
    print(f"The total bill is: ${final_bill}. Each person must pay: ${individual_bill}")
elif tip_choice == "N":
    number_of_people = int(input("How many people are splitting the bill?\n"))
    individual_bill = round(total_bill / number_of_people, 2)
    print(f"Each person must pay: ${individual_bill}")
