import random

print("hello")
x = 9
print(x)
x = "hellow world"
print(x)

stuff = []

stuff.append(9)
stuff.append("hello")
stuff.append(99)
stuff.append(198.84734)
stuff.append([0,1,2,3,4])

print(stuff)

for item in stuff:
    print(item)

# this is a list
newList = []
for i in range(100):
    newList.append(random.randint(0,99999999999))

print(newList[-1])

for i in range(len(newList)):
    print(newList[i])
    newList[i] /= 1000
    print(newList[i])

# tuples

myTuple = (7,8,9)

one,two,three = myTuple

print(f"Numbers: {one}:{two}:{three}")

print(myTuple[0])

# dictionary

myList = [['banana',99],['apples',78],['kiwis',66],['coconuts',54]]

print(myList)

myDict = {'banana':99,'apples':78,'kiwis':66,'coconuts':54}

print(myDict)

print(myDict['banana'])

for key,value in myDict.items():
    print(f"key:{key} => value:{value}")






