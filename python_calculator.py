logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  
  num1 = float(input("What is the first number: "))
  
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    user_reponse = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'exit' to exit the program: ").lower()
    
    if user_reponse == "y":
      num1 = answer
    elif user_reponse == "n":
      should_continue = False
      calculator()
    elif user_reponse == "exit":
      print("Goodbye!")
      should_continue = False

calculator()
