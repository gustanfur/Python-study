#High Card random game with while loop and Boolean condition - pag 125 - Teach your kids to code - Working with arrays
import random
suits = ["clubs", "diamonds", "hearts", "spades"]
faces = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
keep_going = True
while keep_going:
    my_face = random.choice(faces)      #random choice for my card numbers
    my_suit = random.choice(suits)      #random choice for my card suits
    your_face = random.choice(faces)    #random choice for computer card numbers
    your_suit = random.choice(suits)    #random choice for computer suits
    print("I have the", my_face, "of", my_suit)
    print("You have the", your_face, "of", your_suit)
    if faces.index(my_face) > faces.index(your_face):    #compares number position of mine and computers (higher wins)
        print("I win!")
    elif faces.index(my_face) < faces.index(your_face):  #compares number position of mine and computers (higher wins)
        print("You win!")
    else:
        print("It´s a tie!")
    answer = input("Hit [ENTER] to keep going, any key to exit: ")
    keep_going = (answer == "")