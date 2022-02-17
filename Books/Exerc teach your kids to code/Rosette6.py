#Learning loop (step by step) page 60 of the Teach Your Kids to Code

import turtle
t = turtle.Pen()
#Ask the user for the number of circles in their rosette default to 6
number_of_circles = int(turtle.numinput("Number of circles",
                                        "How many circles in your rosette? ", 6)) #6 is the default we choose
for x in range(number_of_circles):
    t.circle(100)
    t.left(number_of_circles)      #We need to divide 360 per number of circles