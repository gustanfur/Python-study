#Learning if statements     -   pag 79 Teach your kids to code

answer = input("Do you want to see a spira? y/n: ")
if answer == "y":
    print("Working")
    import turtle
    t = turtle.Pen()
    t.width(2)
    for x in range (100):
        t.forward(x*2)
        t.left(98)

print("Okay, we are done!")