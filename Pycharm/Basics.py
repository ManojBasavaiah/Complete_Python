from math import ceil

name = "Manoj"
age = 24
# isMale= True
print("Hello, " + "My name is " + name + " and " + str(age) + " years old")
# fruit=input("My favorite fruit is: ")
# print(fruit)

# Strings
phrase="Giraffe Academy"
print(phrase.upper().isupper()) #True
print(phrase.lower())
print(phrase[0])#G
print(len(phrase))#15
print(phrase.index("a", 4)) # 10
# here the search of char starts from 4th index

#numbers
from math import *
num=4
print(ceil(3.7)) #rounds to highest near value >>>4
print(floor(3.9))#rounds to value near to low >>>3
print(sqrt(num))#2.0
#above belongs to math module
print(round(3.5))#4
print(max(5, 200))#200
print(pow(num, 3)) #8.0

