import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_wins = 0
    computer_wins = 0

    while user_wins < 2 and computer_wins < 2:
        user_choice = input("Choose rock, paper, or scissors: ").lower().strip()
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            user_wins += 1
            print("You win this round!")
        else:
            computer_wins += 1
            print("Computer wins this round!")

    if user_wins == 2:
        print("You win the game!")
    else:
        print("Computer wins the game!")

rock_paper_scissors()
