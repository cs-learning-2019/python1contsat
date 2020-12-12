# Focus Learning: Python Level 1 Cont
# Animations
# Kavan Lam
# Dec 12, 2020


# Contents
# 1) Simple animation of a ball moving to the right
# 2) Animation of a ball moving up and down (bouncing off walls)
# 3) Same as 2 but with a square
# 4) Be able to switch the direction of animation with mouse pressed
# 5) Keep track of number of bounces and display on the screen

"""
# Section 1
x = 100
y = 300
def setup():
    size(900, 900)

def draw():
    global x
    global y
    
    background(0, 0, 0)  # Clears the previous frame
        
    fill(255, 0, 0)
    ellipse(x, y, 50, 50)
    
    x = x + 5
"""

"""
# Section 2
x = 450
y = 450
direction = 1  # Either 1 or -1, 1 = move down and -1 = move up
def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction
    
    background(0, 0, 0)  # Clears the previous frame
        
    fill(255, 0, 0)
    ellipse(x, y, 50, 50)
    
    y = y + (5 * direction)
    
    # Detect collisions
    if y >= 900:
        direction = -1 # We need to move up
    elif y <= 0:
        direction = 1 # We need to move down
"""

"""
# Section 3
x = 450
y = 450
direction = 1  # Either 1 or -1, 1 = move down and -1 = move up
def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction
    
    background(0, 0, 0)  # Clears the previous frame
        
    fill(255, 0, 0)
    rect(x, y, 50, 50)
    
    y = y + (10 * direction)
    
    # Detect collisions
    if y >= 850:
        direction = -1 # We need to move up
    elif y <= 0:
        direction = 1 # We need to move down
"""

"""
# Section 4
x = 450
y = 450
direction = 1  # Either 1 or -1, 1 = move down and -1 = move up
case = 1  # Either 1 or 2, 1 = move up and down ....... 2 = move left and right

def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction
    global case
    
    background(0, 0, 0)  # Clears the previous frame
        
    fill(255, 0, 0)
    ellipse(x, y, 50, 50)
    
    if case == 1:
        y = y + (5 * direction)
    elif case == 2:
        x = x + (5 * direction)
        
    # Detect collisions
    if x >= 900:
        direction = -1 # We need to move up
    elif x <= 0:
        direction = 1 # We need to move down
        
    if y >= 900:
        direction = -1 # We need to move up
    elif y <= 0:
        direction = 1 # We need to move down

def mousePressed():
    global case
    if case == 1:
        case = 2
    elif case == 2:
        case = 1
"""

# Section 5
x = 450
y = 450
direction = 1  # Either 1 or -1, 1 = move down and -1 = move up
case = 1  # Either 1 or 2, 1 = move up and down ....... 2 = move left and right
num_bounce = 0  # This is an int

def setup():
    global font1
    
    size(900, 900)
    font1 = loadFont("BodoniMTCondensed-BoldItalic-48.vlw")

def draw():
    global x
    global y
    global direction
    global case
    global num_bounce
    global font1
    
    background(0, 0, 0)  # Clears the previous frame
  
    # Draw the circle 
    pushStyle()
    fill(255, 0, 0)
    ellipse(x, y, 50, 50)
    popStyle()
    
    # Draw some text
    pushStyle()
    textFont(font1, 40)
    text("The num of bounces: " + str(num_bounce), 50, 50)
    popStyle()
    
    if case == 1:
        y = y + (5 * direction)
    elif case == 2:
        x = x + (5 * direction)
        
    # Detect collisions
    if x >= 900:
        direction = -1 # We need to move left
        num_bounce = num_bounce + 1
    elif x <= 0:
        direction = 1 # We need to move right
        num_bounce = num_bounce + 1
        
    if y >= 900:
        direction = -1 # We need to move up
        num_bounce = num_bounce + 1
    elif y <= 0:
        direction = 1 # We need to move down
        num_bounce = num_bounce + 1

def mousePressed():
    global case
    if case == 1:
        case = 2
    elif case == 2:
        case = 1
