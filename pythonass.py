print ("welcome to simple calculator")
user1 = input("enter a number ")
num1 = int(user1)
sign = input(" what sign ")
user2 = input("enter a number ")
num2 = int(user2)
if sign == "+":
    result = num1 + num2
elif sign == "-":
    result = num2 - num2
elif sign == "*":
    result = num1 * num2
elif sign == "/":
    result = num1 / num2
else:
    print("error")
print(f"Your result is: {num1} {sign} {num2} = {result}")

