import random
import sys

print('Welcome to the ROCK, PAPER, SCISSORS game')

# these are the variables with the visuals for the game 

rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# These variables keep track of the number of wins, losses, and ties.

wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

# the main idea is to break down the problem into smaller problems
# e.g. what the player chooses, what the computer chooses
# the nested while loop ( which is the advancd solution

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
        print(rock)
    elif playerMove == 'p':
        print('PAPER versus...')
        print(paper)
    elif playerMove == 's':
        print('SCISSORS versus...')
        print(scissors)

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('PC MOVE - ROCK')
        print(rock)
    elif randomNumber == 2:
        computerMove = 'p'
        print('PC MOVE - PAPER')
        print(paper)
    elif randomNumber == 3:
        computerMove = 's'
        print('PC MOVE - SCISSORS')
        print(scissors)

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1