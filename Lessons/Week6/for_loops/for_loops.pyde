# Focus Learning: Python Level 1 Cont
# For loops
# Kavan Lam
# Oct 23, 2020

# Ex1
# for (a variable) in (something):
for i in range(5):  # the general rule is range will go 1 less than what you say
    print(i)


# Ex2
print("----------------------------")
for num in range(15, 21):
    print(num)
    
    
# Ex3
print("----------------------------")
for p in range(4, 10, 2):
    print(p)
    
    
# Ex4
print("----------------------------")
for countdown in range(10, -1, -1):
    print(countdown)

print("Blastoff!!!")


# Ex5
print("----------------------------")
name = "Kavan"
for character in name:
    print(character)
    

# Ex6
print("----------------------------")
box_size = 7
print("-" * box_size)  # This is the first row

# All the middle rows
for row in range(box_size - 2):
    print("|" + " " * (box_size - 2) + "|")

print("-" * box_size)  # This is the last row
