#calculator

from art import logo 


# Add
def add(num1,num2):
  return num1 + num2

  
# Subtract
def subtract(num1,num2):
  return num1 - n2

  
# Multiply
def multiply(num1,num2):
  return num1 * num2 

  
# Divide
def divide(num1,num2):
  return num1 / num2

operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide, 
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  
  exit = False
  
  while not exit:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
      
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    exiting = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
  
    if exiting == "y":
      num1 = answer
    else:
      exit = True
      calculator()

calculator()
  
  
