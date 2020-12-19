# Focus Learning: Python Level 1 Cont
# Click and Destroy
# Kavan Lam
# Dec 19, 2020

x = [10, 100, 300, 600]
y = [100, 300, 400, 700]
direction = [1, -1, 1, -1]

def setup():
    size(900, 900)
    
def draw():
    global x
    global y
    global direction
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the rectangles
    for index in range(0, len(x)):
        rect(x[index], y[index], 50, 50)
    
    # Update the location of the rectangles
    for index in range(0, len(x)):
        x[index] = x[index] + (3 * direction[index])
    
    # Check for bounce
    for index in range(0, len(x)):
        if x[index] <= 0:
            direction[index] = 1
        elif x[index] >= 850:
            direction[index] = -1
            
def mousePressed():
    global x
    global y
    global direction
    
    # These list will store the information of the surviving sqaures
    x_new = []
    y_new = []
    direction_new = []
    
    for index in range(0, len(x)):
        if mouseX >= x[index] and mouseX <= x[index] + 50 and mouseY >= y[index] and mouseY <= y[index] + 50:
            print("This rect is dead")
        else:
            # This is what happens when the square survives
            x_new.append(x[index])
            y_new.append(y[index])
            direction_new.append(direction[index])
                
    x = x_new 
    y = y_new
    direction = direction_new     
            
            
            
            
