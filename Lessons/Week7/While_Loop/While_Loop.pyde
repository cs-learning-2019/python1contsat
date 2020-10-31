# Focus Learning: Python Level 1 Cont
# While Loops
# Kavan Lam
# Oct 31, 2020

# Ex 1 (Simple example)
# while (condition):   <-- General form
counter = 8
while counter > 0:
    print(counter)
    counter = counter - 2
    
    
print("Hello")  # This is outside the while loop 


# Ex 2
print("------------------------------------")
passby = False
total = 0
while passby == False:
    total = total + 2
    if total > 12:
        print("!!!")
    if total > 20:
        passby = True
        
# In the above example if we did while passby == True: instead then we actually get nothing printed
# this is because passby which is False is not equal to True


# Ex 3
print("------------------------------------")
counter = 10
while counter > 0:
    print("This is amazing!")
    # counter = counter + 1  # This is not a good idea since it will cause an infinite loop
    counter = counter - 1

# Infinite loop is a loop that never stops. It will go on and on until your computer dies.


# Ex 4
print("------------------------------------")
x = 5
y = 0
while x > 0 or y < 3:
    print("Hello " + str(x) + " " + str(y))
    x = x - 1
    y = y + 1
    

# Ex 5
print("------------------------------------")
x = 5
y = 0
while x > 0 or y < 3:
    print("Hello " + str(x) + " " + str(y))
    if x == 4 and y == 1:
        break  # This code will instantly kill the loop
    x = x - 1
    y = y + 1
    
    
# Ex 6
print("------------------------------------")
x = 5
y = 0
while x > 0 or y < 3:
    if x == 3 and y == 2:
        x = x - 1
        y = y + 1
        continue  # Skip this
    print("Hello " + str(x) + " " + str(y))
    x = x - 1
    y = y + 1

    

    






        
        
        
        
