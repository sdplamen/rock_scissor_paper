import random
choices = ['rock', 'scissors', 'paper']
computer = ''
play = ''
count = 1
limit = 6
player_team = 0
computer_team = 0
while count != limit:
    player_choice = input('Rock, Scissors or Paper? ')
    if player_choice == 'r':
        print('Player choice is :        ', choices[0])
        play = choices[0]
    elif player_choice == 's':
        print('Player choice is :        ', choices[1])
        play = choices[1]
    elif player_choice == 'p':
        print('Player choice is :        ', choices[2])
        play = choices[2]
    else:
        print('Invalid choice')
        print('________________________')
        continue
        count -= 1

    computer_choice = random.choice(choices)
    print('Computer choice is :', computer_choice)
    computer = computer_choice
    if player_choice in ("r", "p", "s"):
        play = choices["rps".find(player_choice)]
        print("player choice is: ", play)
        computer_choice = random.choice(choices)
        print("Computer choice ", computer_choice)
        computer = computer_choice
    else:
        print("invalid choice! Please try again")
        print("-" * 75)
        count -= 1
    if player_team > computer_team:
        print('________________________')
        print('Computer team wins by :', player_team - computer_team)
        print('________________________')
        print('Result -', computer_team, ':', player_team)
    elif player_team < computer_team:
        print('________________________')
        print('Player team wins by :', computer_team - player_team)
        print('________________________')
        print('Result -', player_team, ':', computer_team)
    else:
        print('Result -', computer_team, ':', player_team)
        print('________________________')
        print('It\'s a tie >>> No one wins the game')
        print('________________________')
        print('Game finished.')

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice: ").lower()
        return user_choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif ((user_choice == 'rock' and computer_choice == 'scissors') or
(user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper')):
        return "You win!"
    else:
        return "Computer wins!"
def main():
    user_choice = get_user_choice()
    if user_choice != 'invalid':
        computer_choice = get_computer_choice()
        print(f"Computer chose {computer_choice}")
    winner = determine_winner(user_choice, computer_choice)
    print(winner)
if __name__ == "__main__":
    main()
