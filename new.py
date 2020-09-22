import time

import random

options = ["1", "2"]

def print_smooth(message_to_print):
    print(message_to_print)
    time.sleep(3)


def field():
    print_smooth("You find yourself standing in an open field, " 
                 "filled with grass and yellow wildflowers.")
    print_smooth("Rumor has it that a gorgon is somewhere around here, " 
                 "and has been terrifying the nearby village.")

def around_me():
    print_smooth("In front of you is a house.")
    print_smooth("To your right is a dark cave.")

def equipment():
    print_smooth("In your hand you hold your trusty "
                 "but not very effective) dagger.")

def cave():
    for x in range (3):
        value = random.choice(options)
        print_smooth(value)

def main():
    print_smooth("Please enter 1 or 2.")
    entry = input("1.Knock on the door of the house.\n"
                  "2.Peer into the cave.\n")
                     
    if entry == "1": 
           print_smooth("Door of the house.")
    elif entry == "2":
           print_smooth("Into the cave.")
    else:
           if entry != "1" and entry != "2":
                print_smooth("You lost the game. The game is over!")
           else:
                print_smooth("You won the game.")
           
       
    print_smooth("What would you like to do?")
                 
    
def play_over():
    print_smooth("Enter yes or no")
    selection = input("Yes. The game starts over. "
                      "No. The game is over.")
    if selection == "yes":
               print_Smooth("Start over again in choosing your selection.")
    elif selection == "no":
               print_smooth("The player can’t play. The game exits.")
    

def play_game():
    options = []
    cave()
    main()
    play_over()

play_game()
