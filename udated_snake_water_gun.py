import random
lst = ["snake", "water", "gun"]




def snake_water_gun():
    player = input("enter player choice:")
    player_score = 0
    choice = random.choice(lst)
    computer_score = 0
    print(choice)
    if (player == "snake" and choice == "water"):
        print ("player won")
        player_score+= 1
        print(player_score)
    elif ( player == "water" and choice == "snake"):
        print("player lost")
        
        
    elif(player == "water" and choice == "gun"):
        print("player won")
        player_score+= 1
        print(player_score)
        
    elif(player == "gun" and choice == "water"):
        print("player lost")
    
    elif(player == "gun" and choice == "snake"):
        print("player won")
        player_score += 1
        print(player_score)
        
    elif(player == "snake" and choice == "gun"):
        print("player lost")
        

    else:
        print("tie")

    again()
    

def again():
    player_again = input("do you want to play again? press y for yes and n for no:")
    if (player_again == "y"):
        snake_water_gun()
    elif (player_again == "n"):
        print("thank you for playing.")
    else:
        again()
snake_water_gun()
