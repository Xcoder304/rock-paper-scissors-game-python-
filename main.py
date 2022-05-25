import random
from playsound import playsound

def GAME():
    game_option = ["rock","paper","scissors"]
    start_game = str(input("Do you wanna play this game ? "))

    def PLAYGAME():
        computer_selected_value = random.choice(game_option)  
        print(f"1) Rock 2) Paper 3) Scissors\n")
        userinput = str(input("Please Selecte Your Option.. Just Enter Number.... "))
            
        if userinput == "1":
            print(computer_selected_value)
            if computer_selected_value == "paper":
                print(f"you selected Rock","and computer selected",computer_selected_value,"\n","and Computer Win\n")
                playsound('D:\\Coding\\Python\\Projects\\rock-paper-scissors-game\\gameloseAudio.wav')
                print(f"You Loseeee :(\n")
                GAME()

            if computer_selected_value == "scissors":
                print(f"you selected Rock","and computer selected",computer_selected_value,"\n","and You Win\n")
                playsound('D:\\Coding\\Python\\Projects\\rock-paper-scissors-game\\gamewinAudio.wav')
                print(f"You Winnnnnnnn :)\n")

                start_again = str(input("Do you wanna play this game Agian ? "))

                if start_again == "yes":
                    PLAYGAME()
                if start_again == "no":
                    print("byeeee :(")

            if computer_selected_value == "rock": 
                print(f"Woopps! This Look Like a tie\n")
                start_again = str(input("Do you wanna play this game Agian ? "))

                if start_again == "yes":
                    PLAYGAME()
                if start_again == "no":
                    print("byeeee :(")


        if userinput == "2":
            if computer_selected_value == "rock":
                  print(f"you selected Paper","and computer selected",computer_selected_value,"\n","and You Win\n")
                  playsound('D:\\Coding\\Python\\Projects\\rock-paper-scissors-game\\gamewinAudio.wav')
                  print(f"You Winnnnnnnn :)\n")


                  start_again = str(input("Do you wanna play this game Agian ? "))

                  if start_again == "yes":
                      PLAYGAME()
                  if start_again == "no":
                      print("byeeee :(")

            if computer_selected_value == "scissors":
                  print(f"you selected Paper","and computer selected",computer_selected_value,"\n","and Computer Win\n")
                  playsound('D:\\Coding\\Python\\Projects\\rock-paper-scissors-game\\gameloseAudio.wav')
                  print(f"You Loseeee :(\n")
                  GAME()

            if computer_selected_value == "paper": 
                print(f"Woopps! This Look Like a tie\n")
                start_again = str(input("Do you wanna play this game Agian ? "))

                if start_again == "yes":
                    PLAYGAME()
                if start_again == "no":
                    print("byeeee :(")


        if userinput == "3":
            if computer_selected_value == "rock":
                print(f"you selected Scissors","and computer selected",computer_selected_value,"\n","and Computer Win\n")
                playsound('D:\\Coding\\Python\\Projects\\rock-paper-scissors-game\\gameloseAudio.wav')
                print("You Loseeee :(\n")
                GAME()
                
                start_again = str(input("Do you wanna play this game Agian ? "))

                if start_again == "yes":
                   PLAYGAME()
                if start_again == "no":
                    print("byeeee :(")
            
            if computer_selected_value == "paper":
                print(f"you selected Scissors","and computer selected",computer_selected_value,"\n","and You Win\n")
                playsound('D:\\Coding\\Python\\Projects\\rock-paper-scissors-game\\gamewinAudio.wav')
                print("You Winnnnnnnn :)")

                start_again = str(input("Do you wanna play this game Agian ? "))

                if start_again == "yes":
                   PLAYGAME()
                if start_again == "no":
                    print("byeeee :(")
            
            if computer_selected_value == "scissors": 
                print(f"Woopps! This Look Like a tie\n")

                start_again = str(input("Do you wanna play this game Agian ? "))

                if start_again == "yes":
                    PLAYGAME()
                if start_again == "no":
                    print("byeeee :(")                

        
    if start_game == "yes":
        PLAYGAME()
    if start_game == "no":
        print("byeee :)")


GAME()