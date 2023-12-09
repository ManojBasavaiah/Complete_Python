value = input("Enter a value: ")
print(type(value))

try:
    value = float(value)
    if value % 10 == 0:
        print("Value is divisible by 10")
    else:
        print("Value is not divisible by 10")
except ValueError:
    if value.isalpha():
        reversed_value = value[::-1]
        print("Reversed value:", reversed_value)
    else:
        print("Value is not an alphabet")
print(type(value))