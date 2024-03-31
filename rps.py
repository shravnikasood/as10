import random

while True:  # This starts an infinite loop.
    user_action = input("Enter throw (rock, paper, scissors): ")
    ai_action = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose {user_action}, AI chose {ai_action}.\n")

    if user_action == ai_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if ai_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if ai_action == "scissors":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    elif user_action == "scissors":
        if ai_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break  # This exits the loop if the user doesn't type 'yes'.

