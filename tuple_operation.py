thistuple = ("apple", "banana", "cherry")
print(thistuple)

#access elements
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])

#add elements
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#remove items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
