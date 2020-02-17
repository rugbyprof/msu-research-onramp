import random

"""
Random python code to show basic python instructions
"""

# print to screen
print("hello")

# assign var x with 9 
# `x` is now an integer
x = 9

# print it to screen
print(x)

# assign `hello world` to x 
# x is now a string
x = "hello world"

# print it out
print(x)

## lists ################################ 

# create an empty list
stuff = []

# append adds stuff to my list
# notice how the list `stuff` will
# accept all kinds of data types
stuff.append(9)
stuff.append("hello")
stuff.append(99)
stuff.append(198.84734)
stuff.append([0,1,2,3,4])

# print list to screen
print(stuff)

# print out list one item at a time
# (loop through list)
for item in stuff:
    print(item)

# this is another list
newList = []

# fill up list with 100 random numbers between 0 and 99999999999
for i in range(100):
    newList.append(random.randint(0,99999999999))

# print out last item in list
print(newList[-1])

# get length of list with `len`
# then loop that many times accessing
# our list with `i`. This is simply 
# a different way to loop through a list and
# lets us access each element so we might 
# alter the value in the list (like below)
for i in range(len(newList)):
    # print old value
    print(newList[i])

    # alter value at location [i]
    newList[i] /= 1000

    #print new value
    print(newList[i])

## tuples ################################ 

# make a tuple
myTuple = (7,8,9)

# pull the 3 values out with a single assignment
one,two,three = myTuple

# print out our numbers with a "formated" print statement
print(f"Numbers: {one}:{two}:{three}")

# print out the first tuple value
print(myTuple[0])

## dictionary ################################ 

# My attempt an an anology between how dictionaries store data
# vs how lists store data ... (but this is a list :) )
myList = [['banana',99],['apples',78],['kiwis',66],['coconuts',54]]

# print it out
print(myList)

# make a dictionary ( key:value ) pairs
myDict = {'banana':99,'apples':78,'kiwis':66,'coconuts':54}

# print out the dict
print(myDict)

# print out the value of myDict accessed by the `key` banana
print(myDict['banana'])

# loop over a dictionary using `.items` to create little
# tuples of (key,val) pairs for us to assign to `key,val`
for key,value in myDict.items():

    # print out a formatted string with the keys and values
    print(f"key:{key} => value:{value}")






