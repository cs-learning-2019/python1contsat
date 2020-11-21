# Focus Learning: Python Level 1 Cont
# More Loops (with List)
# Nov 14, 2020
# Kavan Lam

# Ex 1
for counter in range(0, 6):
    print(counter)
    

# Ex 2
print("------------------------------------------")
counter = 0
while counter < 6:
    print(counter)
    counter = counter + 1
    

# Ex 3
print("------------------------------------------")
myList = [15, 12, 3, 7]
for item in myList:
    print(item)
 
       
# Ex 4
print("------------------------------------------")
myList = [15, 12, 3, 7]
counter = 0
while counter < len(myList):
    print(myList[counter])
    counter += 1  # This is shorthand notation of counter = counter + 1
    
# Ex 5
print("------------------------------------------")
myList = [15, 12, 3, 7]
for counter in range(4):
    print(myList[counter])
    
# Ex 6
print("------------------------------------------")
myList = [15, 12, 3, 7]
counter = len(myList) - 1
while counter >= 0:
    print(myList[counter])
    counter -= 1
    

# Ex 7
print("------------------------------------------")
food = "peanut butter"
for letter in food:
    print(letter)    
    

# Ex 8
print("-------------------------------------------")
food = "peanut butter"  # 13 characters
counter = 0
while counter < len(food):
    print(food[counter])
    counter += 1
    
    
# Ex 9
print("-------------------------------------------")
greeting = "Hello earthlings!"  # 17 characters =  length of the string
for index in range(len(greeting)-1, -1, -1):
    print(greeting[index])


# Ex 10
print("-------------------------------------------")
greeting = "Hello earthlings!"
counter = len(greeting) - 1
while counter >= 0:
    print(greeting[counter])
    counter = counter - 1
    
# Ex 11
print("-------------------------------------------")
toReverse = "Coding rocks!" # 13 characters
for index in range(len(toReverse)-1, -1, -1):
    print(toReverse[index])


# Ex 12
print("-------------------------------------------")
toReverse = "Coding rocks!"
counter = len(toReverse)-1
while counter >= 0:
    print(toReverse[counter])
    counter -= 1
    

# += is just shorthand notation for adding to a variable. For example, a = a + 3 is the same as a += 3
# -= is just shorthand notation for adding to a variable. For example, a = a - 3 is the same as a -= 3
















    
    
    
    
    
    
