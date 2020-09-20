# Focus Learning
# Python Level 1 Cont
# Kavan Lam
# Sept 20, 2020


def setup(): # This section only gets run one time at the start of your project
    global font1
    global img1
    
    size(900, 600)  # Remember to Tab or 4 spaces
    font1 = loadFont("BodoniMT-48.vlw")
    img1 = loadImage("animal.jpg")
    
    
def draw():  # This is get run over and over again until your project is finished or closed
    global font1
    global img1
    
    background(0, 0, 255) # Colors work by RGB values in Processing. Each number is from 0-255
    strokeWeight(5) # Thickness of the perimeter
    stroke(255, 0, 0)
    rect(0, 200, 50, 100) # First 2 numbers are for position and next two are for the length and width
    line(100, 200, 300, 250)
    
    pushStyle()  # We use the push and pop style so that the fill does not effect the other shapes
    fill(0, 255, 0)
    ellipse(250, 400, 70, 100)
    popStyle()
    
    pushStyle()
    textFont(font1, 24) # The second number is for the font size
    fill(255, 255, 0, 255) # The fourth is the alpha. It is the transparency amount
    text("Hello World", 50, 400)
    popStyle()
    
    image(img1, 600, 100, 150, 100)
    
    
    
