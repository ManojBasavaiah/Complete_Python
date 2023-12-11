Guys = ["sam", "ram", "gowda", "shetty", "rudra", "rudra"]
num = [10, 3, 9, 12, 15.67, -227.2]
# Guys.extend(num)
Guys.append("num")
people=Guys+num
Guys.insert(2, "Gopi")
friends = Guys.copy()
print(Guys.count("rudra"))
Guys.pop()
Guys.remove("shetty")
num
print(friends)
print(people)
print(Guys)
print(num[1:3], num[-4:-1], num[-1])
num.sort()
num.reverse()
print("sorted in decending",num)
Guys[1]="raj" #mutable
print(Guys)
a= input(int('enter the value: '))