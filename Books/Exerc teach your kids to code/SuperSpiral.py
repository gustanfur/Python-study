# Imports the module colorspiral we´ve created
import colorspiral
import random

for n in range(30):
    sides = random.randint(3, 6)
    size = random.randint(25, 75)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    colorspiral.cspiral(sides, size, x, y)
