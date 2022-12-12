# how to clear the console
import os, time
'''os.system("clear")'''

print('''Welcome
\tto
\t\tReplit''')

time.sleep(1)
os.system("clear")

username = input("Username: ")

from replit import audio
import os, time

def play():
    source = audio.play_file('poor.wav')
    
    source.paused = False # unpause the playback
    while True:
    # Start taking user input and doing something with it
        pause = int(input('Press 2 to Pause')) #giving the user option to pause playback
        if pause == 2:
            source.paused = True # let's pause the file
            return # let's go back from this play() subroutine
        else:
            continue
while True:
    # clear the screen 
    os.system("clear")
    print('My IPod music player')
        
    # Show the menu
    time.sleep(1)
    print('Press 1 to Play')
    time.sleep(1)
    print('Press 2 to Pause')
    time.sleep(1)
    print('Press anything else to see menu again.')
        
    # take user's input
    userInput = int(input())
    if userInput == 1:
        print('Playing some proper tunes!')
        play()
    elif userInput == 2:
        pause()
    else:
        continue
    # check whether you should call the play() subroutine depending on user's input
