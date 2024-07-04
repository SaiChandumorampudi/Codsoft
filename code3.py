import random
while True:

    user_choice=input("Enter a your choice (Rock, Paper, Scissors): ")
    possible_choice = ["Rock", "Paper", "Scissors"]
    computer_choice=random.choice(possible_choice)
    print("\nYou chose [user_choice), computer chose (computer_choice).\n")
    
    if user_choice == computer_choice:
        print("Both have chosen the same It's a tie..!")
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print("Rock beats scissors!.. You win..Hurray!")
        else:
            print("Paper beats rock! You lose..better luck next time")
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print("Paper beats rock! You win. great keep going!")
        else:
            print("Scissors beats paperl You lose..")
    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            print("scissors beats paper! you win...Amazing")
        else:
            print("Rock beats scissors! You lose..dont worry try again buddy")

    play_again=input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break