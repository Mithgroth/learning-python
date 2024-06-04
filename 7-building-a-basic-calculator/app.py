# Python inputs are string by default
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2

print(result)

# Need to convert them to type
result = float(num1) + float(num2)
print(result)