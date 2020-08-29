no_1 = int(input("enter first number: "))
op = input("input operator: ")
no_2 = int(input("enter second number: "))
if op == "+":
    print(no_1 + no_2)
elif op == "-":
    print(no_1 - no_2)
elif op == "*":
    print(no_1 * no_2)
elif op == "/":
    print(no_1 / no_2)
else:
    print("Syntax Error")