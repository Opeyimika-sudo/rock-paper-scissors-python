import random

welcome_address = "This game was developed with you in mind and in hopes that you will be reminded of the joy of playing rock, paper, scissors. You will be playing against the computer. I am rooting for you to win."
game_instructions = "All you have to do is pick one of the following - R for Rock, P for Paper and S for Scissors. Just write the first letter of your option. For example, if you want to choose Rock, just type R. Goodluck." 
print(welcome_address)
print(game_instructions)
game_list = ["R", "P", "S"]


def run_game():
    computer_input = random.choice(game_list)
    # print(computer_input)
    user_input = input("Please pick an option between 'R', 'P' and 'S' ")
    user_input = str(user_input).upper()
    # print(user_input)
    try:
        if (user_input in game_list):
            print("Your option %s is valid. " % user_input)
            
            if(user_input == "P"):
                if(computer_input == "P"):
                    print("This is a draw. You chose %s and the computer chose %s. You have to go again. Goodluck." % (user_input, computer_input))
                    run_game()
                elif(computer_input == "R"):
                    print("You win. You chose %s and the computer chose %s." % (user_input, computer_input))
                elif(computer_input == "S"):
                    print("You lose. You chose %s and the computer chose %s." % (user_input, computer_input))

            elif(user_input == "S"):
                if(computer_input == "S"):
                    print("This is a draw. You chose %s and the computer chose %s. You have to go again. Goodluck." % (user_input, computer_input))
                    run_game()
                elif(computer_input == "P"):
                    print("You win. You chose %s and the computer chose %s." % (user_input, computer_input))
                elif(computer_input == "R"):
                    print("You lose. You chose %s and the computer chose %s." % (user_input, computer_input))

            elif(user_input == "R"):
                if(computer_input == "R"):
                    print("This is a draw. You chose %s and the computer chose %s. You have to go again. Goodluck." % (user_input, computer_input))
                    run_game()
                elif(computer_input == "S"):
                    print("You win. You chose %s and the computer chose %s." % (user_input, computer_input))
                elif(computer_input == "P"):
                    print("You lose. You chose %s and the computer chose %s." % (user_input, computer_input))
            
        else:
                print("Offer a valid option")
                run_game()
    except:
        print("This is not a string")

run_game()


