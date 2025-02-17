PI = 3.14

def circumference(radius):
    return PI * radius*2


def area(radius):
    return PI * radius*radius

def main():
    print(area(4.56))
    print(circumference(34.6))

main()
"""The difference lies in the parameter/argument passing
  When you use a global variable, there is no need to use that variable as argument
  This is because the function already orders the operation on those
  variables, and there would be no need to pass arguments since the 
  values have already been set
  Unless you're introducing a variable that has not been
  assigned in a global scope, that would be when you pass that 
  variable as a parameter...(The variable ought to be used in the function
  and passed as a parameter if it is to be used"""