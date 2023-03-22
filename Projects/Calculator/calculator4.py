# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multliply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Tax
def tax(num1):
    '''Take the state name and the price to return its corresponding value added tax'''

    state_tax = {
        'AL': 9.24,
        'AK': 1.76,
        'AR': 9.47,
        'AZ': 8.4,
        'CA': 8.82,
        'CO': 7.77,
        'CT': 6.35,
        'DC': 6.0,
        'DE': 0.0,
        'FL': 7.01,
        'GA': 7.35,
        'HI': 4.44,
        'IA': 6.94,
        'ID': 6.02,
        'IL': 8.81,
        'IN': 7.00,
        'KS': 8.7,
        'KY': 6.0,
        'LA': 9.55,
        'MA': 6.25,
        'MD': 6.0,
        'ME': 5.50,
        'MI': 6.0,
        'MN': 7.49,
        'MO': 8.29,
        'MS': 7.07,
        'MT': 0.0,
        'NC': 6.98,
        'ND': 6.96,
        'NE': 6.94,
        'NH': 0.0,
        'NJ': 6.6,
        'NM': 7.84,
        'NV': 8.23,
        'NY': 8.52,
        'OH': 7.22,
        'OK': 8.97,
        'OR': 0.0,
        'PA': 6.34,
        'RI': 7.0,
        'SC': 7.44,
        'SD': 6.4,
        'TN': 9.55,
        'TX': 8.2,
        'UT': 7.19,
        'VA': 5.75,
        'VT': 6.24,
        'WA': 9.29,
        'WI': 5.43,
        'WV': 6.52,
        'WY': 5.22
    }

    state = input("State abbriviation: ").upper()
    result = num1 * (1 + (state_tax[state] / 100))
    return result 


# Catalog 
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "tax": tax
}


def calculator():
  num1 = float(input("ON:\n"))
  
  #Set a flag value to initiate while loop
  prompt = True
  while prompt == True:
    operation_symbol = input()
    if operation_symbol == "tax":
      print(f"Result: {tax(num1)}\n")
      calculator()
    num2 = float(input())
    result = operations[operation_symbol](num1, num2)
    print(f"Result: {result}\n")

    next_step = input()
    if next_step == "":
      num1 = result #retun result to be used in new calculation loop
      print(num1)
    else:
      prompt = False
      calculator() #use recursion to restart setting once reach the end of function 

calculator()

    
  

