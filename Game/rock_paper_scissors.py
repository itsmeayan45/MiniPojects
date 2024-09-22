import random

def rock_paper_scissors():
    moves = ['rock', 'paper', 'scissors']
    
    while True:
        user_move = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
        if user_move == 'quit':
            break
        if user_move not in moves:
            print("Invalid input, try again.")
            continue
        
        computer_move = random.choice(moves)
        print(f"Computer chose {computer_move}")

        if user_move == computer_move:
            print("It's a tie!")
        elif (user_move == 'rock' and computer_move == 'scissors') or \
             (user_move == 'scissors' and computer_move == 'paper') or \
             (user_move == 'paper' and computer_move == 'rock'):
            print("You win!")
        else:
            print("You lose!")

rock_paper_scissors()