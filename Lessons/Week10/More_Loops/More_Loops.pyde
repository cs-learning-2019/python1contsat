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
