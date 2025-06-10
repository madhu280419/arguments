num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator: ")
if operator == "+":
    print(f"addition of 2 numbers is {num1 + num2}")
elif operator == "-":
    print(f"subtraction of 2 numbers is {num1 - num2}")
elif operator == "*":
    print(f"multiplication of 2 numbers is {num1 * num2}")
elif operator == "/":
    print(f"division of 2 numbers is {num1 / num2}")
else:
    print("invalid operator")
