# List in Python
name = ["Abel", "Abenezer"] 
numbers = [1,2,3] 
combo = ["Abel", 2, 3] #Python list can store different datatypes

########## Basics of List ##########
# Printing items inside the list using for loop
for item in combo:
    print(item)
    
# Printing specific element inside the list
print(combo[0])

# Adding additional element inside the list
numbers.append(4)
print(numbers)

# Adding additional element inside the list, by setting a position insert(position,element)
numbers.insert(1,100)
print(numbers)

# Adding more items in the list within the last element. 
numbers.extend([300,400,25])
print(numbers)

# Sorting a list in ascending order
numbers.sort()
print(numbers)

# Sorting a list in reverse order
numbers.reverse()
print(numbers)

# Removing element inside the list
numbers.remove(400)
print(numbers)


########## Basics of Dictionaries ##########
alphaNum ={
    "One":1,
    "Two":2,
    "Three":3
}

# Accessing the value of key
print(alphaNum["Two"])

# Printing all the key items inside the dictionary
for items in alphaNum:
    print(items)
    
# Printing all the value items inside the dictionary
for items in alphaNum.keys():
    print(alphaNum[items])
    
    
    
########## Basics of Tupple ##########
coordinates = (2,3)
print(coordinates)