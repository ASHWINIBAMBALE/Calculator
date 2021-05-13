def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
operations={
          "+":add,
           "-":subtract,
           "*":multiply,
            "/":divide
          }


def calculator():
  num1=float(input("Enter the first number:"))
  for symbol in operations:
    print(symbol)
  shld_con=True
  while shld_con:
    operation_Symbol=input("Enter the opeartion from :")
    num2=float(input("Enter the nxt number:"))
    calculation=operations[operation_Symbol]
    result=calculation(num1,num2)
    print(f"{num1} {operation_Symbol} {num2}={result}")
  
    cont=input(f"Type 'Y' to continue with {result} and 'N' to end: " ).lower()
    if cont=="y":
      num1=result
    else:
      shld_con=False
      exit()
calculator()


