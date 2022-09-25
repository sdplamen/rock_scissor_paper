import random, sys
print('камък, ножица, хартия')
# These variables keep tracks of the nimber of wins, losses, ties.
wins = 0
losses = 0
ties = 0
while True:# The main game loop.
    print('%s печалби, %s загуби, %s равни' % (wins, losses, ties))
    while True: # The player input loop
        print('Моля, натисни бутон с избора си: (к)амък (х)артия (н)ожица or (и)злез')
        move = input()
        if move == 'и':
            sys.exit() #Quit the program
        if move == 'к' or move == 'х' or move == 'н':
            break # Break out of the player input
        print('Избери едно от к, х, н или и.')
    # Display what player choose
    if move == 'к':
        print('камък срещу ')
    elif move == 'х':
        print('хартия срещу ')
    elif move == 'н':
        print('ножица срещу ')
    # Display what computer choose
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        compMove = 'к'
        print('камък')
    elif randomNumber == 2:
        compMove = 'х'
        print('хартия')
    elif randomNumber == 3:
        compMove = 'н'
        print('ножица')
    # Display and record the win / loss / tie
    if move == compMove:
        print('Равни.')
        ties = ties + 1
    elif move == 'к' and compMove == 'н':
        print('Спечели.')
        wins = wins + 1
    elif move == 'х' and compMove == 'к':
        print('Спечели.')
        wins = wins + 1
    elif move == 'н' and compMove == 'х':
        print('Спечели.')
        wins = wins + 1
    elif move == 'к' and compMove == 'х':
        print('Загуби.')
        losses = losses + 1
    elif move == 'х' and compMove == 'н':
        print('Загуби.')
        losses = losses + 1
    elif move == 'н' and compMove == 'к':
        print('Загуби.')
        losses = losses + 1