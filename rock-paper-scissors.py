import random

name = input("What's your name? ")

while True:
    options = ["rock", "paper", "scissors"]
    player_input = input("Choose a word: ")
    player_input = player_input.lower()
    computer_input = random.choice(options)
    print(f"{player_input} vs {computer_input}")
    
    if not player_input in options:
        print("Choose one of the following: rock, paper or scissors") 
        continue
    
    if player_input == computer_input:
        print("It's tie!")
    elif player_input == "rock" and computer_input == "scissors":
        print(f"{name} won!")
        break
    elif player_input == "paper" and computer_input == "rock":
        print(f"{name} won!")
        break
    elif player_input == "scissors" and computer_input == "paper":
        print(f"{name} won!")
        break
    else:
        print(f"{name} lost!")        
    
    new_game = input("Would you like to play another game?(y/n) ")
    if new_game.lower() == "y":
        player_input = False
    else:
        print(f"Thanks for playing, {name}!")
        break
    
                

    
        

    
   