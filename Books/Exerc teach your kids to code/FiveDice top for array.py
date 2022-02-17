#Five dice game - a good way to learn arrays - pag 129 - Teach your kids to code
import random
#Game loop
keep_going = True
while keep_going:
    #"Roll" five random dice
    dice = [0,0,0,0,0]                  #Set up an array for five values dice [0]-dice[4]
    for i in range(5):                      #"Roll" a random number from 1-6 for all 5 dice
        dice[i] = random.randint(1, 6)      #this will roll 5 dices and add the index from 1-5
    print("You rolled:", dice)               #Print out the dice values
    #sort them
    dice.sort()
    #Check for five of a kind, four of a kind, three of a kind
    #Yahtzee - all five dice are the same
    if dice[0] == dice[4]:
        print("Yahtzee!")
    #FourOfaKind - first four are the same, or last four are the same
    elif (dice[0] == dice[3]) or (dice[1] == dice[4]):
        print("Four of a kind!")
    #Three of a kind - first three, middle three, or last three are the same
    elif (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
        print("Three of a kind!")
    keep_going = (input("Hit [ENTER] to keep going, any key to exit: ") == "")


#dice[i] isso faz os dados rodarem 5 vezes, e o random.randint(1, 6) vai adicionando valor de 1 a 5 em cada posição
#do dado