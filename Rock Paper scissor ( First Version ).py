def  rock_paper_scissor():

    print('Rock Paper scissor game\n')

    x=input('Press Enter to contiue\n')
    while True:
        import random
        computer = random.randint(1, 3)
        user = int(input('Enter your choice \n 1. Rock \n 2. Paper \n 3. Scissor\n 4. Exit \n' '1 or 2 or 3 : '))
        if (user == computer):
            print('Tie')
        elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
            print('Computer win')
        elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2) :
            print('You win')
        elif (user == 4):
            break
        else:
            print('Invalid input')
print( '           ******* MINI GAMES ******' )
print('                   ***********' )
a=input('Press Enter to contiue\n')
if a=='':
    b=int(input('which game would you like to play\n 1. Rock Paper Scissor \n 2. Exit \n 1 or 2 : '))
    if b==1:
        rock_paper_scissor()
    else:
        exit()