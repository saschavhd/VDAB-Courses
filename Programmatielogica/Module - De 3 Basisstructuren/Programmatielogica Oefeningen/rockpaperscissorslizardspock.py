from random import randint
from os import system, name
from time import sleep

print("Welcome to rock-paper-scissors!")
rounds = int(input("Enter the amount of rounds you want to play: "))

playerScore, computerScore = 0, 0

for i in range(1, rounds+1):
    print("Round: {}/{}".format(i, rounds))
    print("Current score - Player: {} <-> Computer: {}".format(playerScore, computerScore))
    playerChoice = int(input(
    '''
    Choose your play:
    1. Rock
    2. Paper
    3. Scissors
    '''
    ))
    computerChoice = randint(1, 3)

    if playerChoice == computerChoice:
        print('Draw')

    elif playerChoice == 1:
        if computerChoice == 2:
            print("Computer wins!")
            computerScore += 1
        else:
            print("Player wins!")
            playerScore += 1

    elif playerChoice == 2:
        if computerChoice == 1:
            print("Player wins!")
            playerScore += 1
        else:
            print("Computer wins!")
            computerScore += 1

    elif playerChoice == 3:
        if computerChoice == 1:
            print("Computer wins!")
            computerScore += 1
        else:
            print("Player wins!")
            playerScore += 1

    sleep(2)
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if playerScore > computerScore:
    print("Player wins: {} to {}".format(playerScore, computerScore))
elif computerScore > playerScore:
    print("Computer wins: {} to {}".format(computerScore, playerScore))
else:
    print("It's a draw! Score: {}".format(playerScore))
