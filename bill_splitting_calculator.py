print("Welcome to the bill splitting calculator")
bill = float(input("What is the total bill?\n"))
tip = int(input("What is your desired tip percentage?\n"))
people_paying = float(input("How many people are splitting the bill\n"))

tip_amount = (tip / 100) * bill

bill_total = bill + tip_amount

split_total = round(bill_total / people_paying, 2)
split_total = "{:.2f}".format(split_total)

print(f"Each person is paying {split_total}")
