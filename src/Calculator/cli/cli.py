from Calculator.core.operations import add, sub, div, mul



print("1: add")
print("2: sub")
print("3: div")
print("4: mul")

choice = input("choice 1, 2, 3 or 4")

num1 = int(input("type your first number:"))
num2 = int(input("type your second number:"))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", sub(num1, num2))
elif choice == '3':
    print(num1, "/", num2, "=", div(num1, num2))
elif choice == '4':
    print(num1, "*", num2, "=", mul(num1, num2))
else: 
    print("invalid input")


