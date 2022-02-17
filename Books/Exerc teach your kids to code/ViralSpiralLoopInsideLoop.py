#Viral Spiral - loop inside antother loop   - page 68  - Teach your kids to code

import turtle
t = turtle.Pen()
t.penup()       #this is to lift the pen right from the start and avoid writting
turtle.bgcolor("black")
#Ask the user for the number os sides, default 4, min 2, max 6
sides = int(turtle.numinput("Number of side",
                            "How many sides in your spiral of spirals (2-6)?", 4,2,6))
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
#Our outer spiral loop
for m in range(100):
    t.forward(m*4)
    position = t.position()         #Remember this corner of the spiral
    heading = t.heading()           #Remember this direction we were heading
    print(position, heading)
#Our inner spiral loop
#Draws a little spiral at each corner of the big spiral
    for n in range(int(m/2)):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.forward(2*n)
        t.right(360/sides - 2)
        t.penup()
    t.setx(position[0])             #Go back to the bif spiral´s x location
    t.sety(position[1])             #Go back to the big spiral´s y location
    t.setheading(heading)            #Point in the big spiral´s heading
    t.left(360/sides + 2)           #Aim at the next point on the big spiral
