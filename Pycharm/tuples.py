coordinates=(4,5)
# coordinates[0]=6 TypeError: 'tuple' object does not support item assignment: immutable
print(coordinates)

cordinate=[(4,5), (6,3), (2,6)]
cordinate[1]=4
cordinate[0]=(5,"happy")
print(cordinate)

items=("jar", 5)
print(items)