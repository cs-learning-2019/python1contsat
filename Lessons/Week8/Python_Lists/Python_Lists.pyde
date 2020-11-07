# Focus Learning: Python Level 1 Cont
# Python Lists
# Kavan Lam
# Nov 7, 2020 

# If we had 4 students in a class and we want to program their ages we can do this
age1 = 10
age2 = 12
age3 = 9
age4 = 11

# This is not a very good method since if we had 1000 students we would need 1000 variables

# Lets do this using a better method
ages = [10, 12, 9, 11]  # This is a Python List, we use square brackets to create a List

print(ages)
print(ages[0])  # In a list the first thing is always index 0. We always start conuting from 0

# Lets take a look at the worksheet now
print("--------------------------------------------------")
pets = [3, 5, 1, 9, 0, 2]

print(pets[0])
print(pets[3])
print(pets)

pets[2] = 6
pets[5] = pets[5] + 3
print(len(pets))  # len stands for length
print(len("Hello")) # You can also find the length of a string
print(pets)

# print(pets[8]) we can not do this since there is no such thing as index 8 in our list
print(pets[-1])  # if we give negative number then python will go in reverse starting from the last thing

print("----------------------------------------------")
students = [10, 12, 9, 8, 13, 11]
students.append(13)  # append means add to the end
print(students)

students.pop(1)  # pop expects you to give it an index
print(students)

students.pop()  # If you do not provide an index python will automatically remove the last thing
print(students)
