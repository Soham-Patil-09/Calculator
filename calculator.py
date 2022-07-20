#mini project that is calci

first=input("enter first numer  ; ")

op = input("choose any one (+,-,*,/,%):")

second = input("enter the second number :")

first = int (first)

second =int (second)

if op == "+":
    print(first + second)

elif op == "-":
    print(first - second)

elif op == "*":
    print(first * second)

elif op == "/":
    print(first / second)

elif op =="%":
    print(first % second)

else:
    print("invalid inputs")