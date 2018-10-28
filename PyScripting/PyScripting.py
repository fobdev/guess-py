import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def dif_select():
    difficulty = int(input("Select a difficulty: \n\n[1]> EASY (50 lifes)\n[2]> MEDIUM (20 lifes)\n[3]> HARD (5 lifes)\n\n$- "))
    if ((difficulty <= 0) or (difficulty >= 4)):
        input("\nInvalid value, try again.")
        clear()
        alg(0)
    else:
        if difficulty == 1:
            return 50
        if difficulty == 2:
            return 20
        if difficulty == 3:
            return 5

def alg(sucess):
    lifes = dif_select()
    if sucess == 1:
        exit(0)
    else:
        init = int(input("\nSet a initial range: "))
        end = int(input("Set a final range: "))
        
        if end < init:
            input("\nINIT needs to be greater than END, try again.\n")
            clear()
            alg(0)
        
        hidden = random.randint(init, end)
        
        while 1:
            limit = 20
            range_limit = end - init
            if range_limit < limit:
                print("\nEND - INIT = {}\nEND - INIT must be greater than {}, try again.\n".format(range_limit ,limit))
                alg(0)
            else:
                break

        while 1:
            guess = int(input("\nTry a number between [{}] and [{}]: ".format(init,end)))
            if guess < init:
                print("\n[{}] is smaller than INIT, please use a value between [{}] and [{}]".format(guess, init, end))
            if guess > end:
                print("\n[{}] is larger than END, please use a value between [{}] and [{}]".format(guess, init, end))
            else:
                if lifes == 0:
                    print("Game over, run out of lifes! Good luck next time...")
                    break
                else:
                    if (guess == hidden) & (guess > init) & (guess < end):
                        print("\nYou found the hidden value! It is [{}]!".format(hidden))
                        alg(1)
                        break
                    if (guess > hidden) & (guess >= init) & (guess <= end):
                        lifes -= 1
                        print("\n[{}] is greater than the hidden value, try again!\n[{}] lifes remaining".format(guess, lifes))
                    if (guess < hidden) & (guess >= init) & (guess <= end):
                        lifes -= 1
                        print("\n[{}] is smaller than the hidden value, try again!\n[{}] lifes remaning".format(guess, lifes))
    
alg(0)