

import random

def choose_random():
    return random.randint(0,2)

    if input_1 == input_2: 
        return "tie"
    elif input_1 == 0 and imput_2 == 1:
        return "lose"
    elif input_1 == 0 and input_2 == 2:
        return "win"
    elif input_1 == 1 and input_2 == 0:
        return "win"
    elif input_1 == 1 and input_2 == 2:
        return "lose"
    elif input_1 == 2 and input_2 == 0:
        return "lose"
    elif input_1 == 2 and input_2 == 1:
        return "win"
    
def check_win(input_1, input_2):
    win_options = ["tie","win","lose"]
    diff = input_1 - input_2
    return win_options[diff % 3]

    if diff == 0:
        return "tie"
    elif diff % 3 == 2:
        return "loss"
    elif diff % 3 == 1:
        return "win"
    



def get_user_input():
    valid_input = False
    while not valid_input:
        user_input = input("rock (0). paper (1), or scissors(2). (Q) to quit: ")
        if user_input == "q":
            return user_input
        elif user_input == "0" or user_input == "1" or user_input == "2":
            valid_input = True
            return int(user_input)
        else:
            print ("NOOOO!")


game_going = True
options = ["rock", "paper", "scissors"]
while game_going:
    user_input = get_user_input()
    if user_input == "q":
        break
    computer_input = choose_random()
    print(f"You chose: {options [user_input]}. computer chose: {options[computer_input]}.")
    print(check_win(user_input,computer_input))



