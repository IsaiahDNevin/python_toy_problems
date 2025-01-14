import random
import time


def print_starting_message():
    messages = ["Rock", "Paper", "Scissors"]
    for message in messages:
        print(message)
        time.sleep(.5)



def get_user_input():
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")


# unittest number 1 :)
def get_computer_choice():
    rand_num = random.randint(1, 3)
    if rand_num == 1:
        return "rock"
    elif rand_num == 2:
        return "paper"
    elif rand_num == 3:
        return "scissors"
    


def run_game():
    print_starting_message()
    computer_choice = get_computer_choice()
    users_input = get_user_input()
    print(f"Computer chose: {computer_choice}")
    if users_input == computer_choice:
        return "tie"
    elif (users_input == "rock" and computer_choice == "scissors") or \
         (users_input == "scissors" and computer_choice == "paper") or \
         (users_input == "paper" and computer_choice == "rock"):
        return "player"
    else:
        return "computer"



def evaluate_winner(state: {}):
    if state["computer"] < state["player"]:
        return "You won!!"
    else:
        return "You lose :("


# dont test
def initialize(run_times = 3, state = {"player": 0, "computer": 0}, cb = lambda s: print(s)):
    if run_times == 0:
        return cb(state)
    
    game_output = run_game()

    if game_output == "tie":
        print("Yike's, that's a tie! Try again!")
        return initialize(run_times, state, cb)
    
    new_state = state.copy()
    new_state[game_output] += 1

    return initialize(run_times - 1, new_state, cb)
    

initialize(print(cb=lambda s: evaluate_winner(s)))

