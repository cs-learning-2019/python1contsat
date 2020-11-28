# Focus Learning: Python Level 1 Cont
# User interaction using the keyboard and mouse 
# Kavan Lam
# Nov 28, 2020

# Contents
# 1) How to get keyboard input using key and keyCode
# 2) How to get mouse input (the position of the mouse)
# 3) How to move an object using WASD or the arrow keys
# 4) How to move an object using the mouse

# Section 1
"""
def setup():
    size(900, 900) 

def draw():
    background(0, 0, 0)
    
    pushStyle()
    fill(255, 0, 0)
    rect(100, 100, 50, 50)
    popStyle()

def keyPressed():
    if key == "W" or key == "w":
        print("Move up")
    elif key == "A" or key == "a":
        print("Move Left")
    elif key == "S" or key == "s":
        print("Move Down")
    elif key == "D" or key == "d":
        print("Move Right")
"""

# Section 2
"""
def setup():
    size(900, 900) 

def draw():
    background(0, 0, 0)
    
    pushStyle()
    fill(255, 0, 0)
    rect(100, 100, 50, 50)
    popStyle()

def mousePressed():
    print("The mouse was pressed")
    print(mouseX, mouseY)
"""

# Section 3
"""
x = 100
y = 100
def setup():
    size(900, 900) 

def draw():
    global x
    global y
    
    background(0, 0, 0)
    
    pushStyle()
    fill(255, 0, 0)
    ellipse(x, y, 50, 50)
    popStyle()
    
def keyPressed():
    global x
    global y
    
    if keyCode == UP:
        y = y - 10
    elif keyCode == LEFT:
        x = x - 10
    elif keyCode == DOWN:
        y = y + 10
    elif keyCode == RIGHT:
        x = x + 10
"""

# Section 4
def setup():
    size(900, 900) 

def draw():
    global x
    global y
    
    background(0, 0, 0)
    
    pushStyle()
    fill(0, 0, 0)
    stroke(255, 0, 0)
    ellipse(mouseX, mouseY, 50, 50)
    popStyle()

        

        
        
        
        
    
    

    
