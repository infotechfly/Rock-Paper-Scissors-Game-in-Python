import random

def get_user_choice():
    print("Enter your choice (rock, paper, or scissors):")
    user_choice = input().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose either rock, paper, or scissors:")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    
    return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors game!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        print("\nDo you want to play again? (yes/no):")
        play_again = input().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_game()
