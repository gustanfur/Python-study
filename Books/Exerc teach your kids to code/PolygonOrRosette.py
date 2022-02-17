import turtle
t = turtle.Pen()
#Ask the user for the number of sides or circles, default to 6
number = int(turtle.numinput("Number of sides or circles",
                             "How many sides or circles in your shape?", 6))
#ASk the user whether they want a polygon or a rosette
shape = turtle.textinput("Which shape do you want?",
                         "Enter 'p' for the polygon or 'r' for the rosette: ")
for x in range(number):
    if shape == 'r':                #User selected rosette
        t.circle(100)
    else:                           #Default to polygon
        t.forward(150)
    t.left(360/number)