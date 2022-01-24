#Nov 5
#Saad Zaki
ifchance= False
fiveToNine= False
main=0
chance=0
game=1
win=0
loss=0
dice=0
play=True
while (play):
    import random
    print("Game:",game)
    while (not(fiveToNine)):
        try:
            main=int(input("Enter your number for main (5-9):"))
            if main>=5 and main<=9:
                fiveToNine=True
        except:
            print("Please enter a valid number")
    dice = random.randint(2,12)
    print("\nYou rolled a:", dice)
    if dice==main:
        print("\nYou win")
        win+=1
    elif dice==2 or dice==3:
        print("\nYou lose")
        loss+=1
    elif dice==11 or dice==12:
        if main==5 or main==9:
            print("\nYou lose")
            loss+=1
            #no need to write win=False cuz its already false
        elif main==6 or main==8:
            if dice==11:
                print("\nYou lose")
                loss+=1
            elif dice==12:
                print("\nYou win")
                win+=1
        elif main==7:
            if dice==11:
                print("\nYou win")
                win+=1
            elif dice==12:
                print("\nYou lose")
                loss+=1
    else:
        chance=dice
        print("Your Chance is", chance,"and your Main is",main,"\n")
        while (not(ifchance)):
            dice = random.randint(2,12)
            print("You Rolled a", dice)
            if dice==chance:
                print("\nYou win")
                win+=1
                ifchance=True
            elif dice==main:
                print("\nYou lose")
                loss+=1
                ifchance=True
    fiveToNine=False
    ifchance= False
    play= input("Do you want to play again (yes/no)")
    while not(play=="yes" or play=="no"): 
        play= input("Please enter 'yes' or 'no':")
    game+=1
    if play!=("yes"):
        play=False
        print("Thanks for playing Hazard Dice!")
        print("You played:",game,"games(s), Won:",win,"time(s), \
and Lost:",loss,"time(s)")
