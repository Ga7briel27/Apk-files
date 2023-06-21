import math
from turtle import Turtle
#initialize variable
#Create shape function
#Circle
def drawcircle (t, x, y,radius):
    """Draws a circle with the given center point and radius."""
    t.up()
    t.goto(x+radius,y)
    t.setheading(90)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0 * math.pi * radius/120.0)
#Star
def drawstar (t,x):
    for i in range (5):
        t.forward(x)#moving turtle 65 units forward
        t.right(144)#rotating turtle 130  degree right

#Rectangle  
def drawrectangle (t,side):#length of each side
     #drawing first side
       
      t.forward(side) #Forward turtle by l units
      t.left(90) #Turn turtle by 90 degree
    # drawing second side
      t.forward(side) #Forward turtle by w units
      t.left(90) #Turn turtle by 90 degree
    # drawing third side
      t.forward(side)#Forward turtle by l units
      t.left(90)  #Turn turtle by 90 degree
    # drawing fourth side
      t.forward(side)#Forward turtle by w units
      t.left(90)#Turn turtle by 90 degree

#square
def drawsquare(t, side):#Length of each side
     #drawing first side
     t.forward(side) #Forward turtle by x units
     t.left(85)#turn turlte by 85 degrees
     #drawing second side
     t.forward(side)
     t.left(85) #turn turtle by 85 degrees
     #drawing third side
     t.forward(side) #Forward turtle by X units
     t.left(85)#Turn turtle by 85 degrees

#Hexagon
def drawhexagon (t,x):
    for i in range(6): # executing loop 6 times for 5 sides
        t.forward(x) #Move forward by 80 units
        t.left(300) #turn left by 200 degrees

def main():
   while True:
       print("You can choose from Square, Circle, Star, and Hexagon for the shape")
       print("Enter "" to exit.")
       shape=input("Select the shape you want to draw:")#User enters the size
       if str(shape)=="":
           break
           exit()
       sz=int(input("Select the size for the shape:"))
       if str(shape)=="circle":
        #drawCircle(Turtle(), x, y, radius)
           x=0
           y=0#Set the center of the shape
           drawcircle(Turtle(), x, y, sz)
       elif str(shape)=="square":
          drawsquare(Turtle(),sz)
       elif str(shape)=="star":
           drawstar(Turtle(),sz)
       elif str(shape)=="hexagon":
           drawhexagon(Turtle(),sz)
       elif str(shape)=="rectangle":
            drawrectangle(Turtle(),sz)

if __name__ == "__main__":
   main()
    
        
         

          
     
     
      
    
    


