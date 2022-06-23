# Création d'un jeu de oxo avec la machine 


from random import randint
import time
from choice_machine import verification_choice_machine
from verification_winner import winner
from gameMain import game_main

print("""
                                                  
                      $$ |                                    $$ |                     
 $$$$$$\  $$$$$$$\  $$$$$$\    $$$$$$\                   $$$$$$$ | $$$$$$\  $$\    $$\ 
 \____$$\ $$  __$$\ \_$$  _|  $$  __$$\                 $$  __$$ |$$  __$$\ \$$\  $$  |
 $$$$$$$ |$$ |  $$ |  $$ |    $$ /  $$ |                $$ /  $$ |$$$$$$$$ | \$$\$$  / 
$$  __$$ |$$ |  $$ |  $$ |$$\ $$ |  $$ |                $$ |  $$ |$$   ____|  \$$$  /  
\$$$$$$$ |$$ |  $$ |  \$$$$  |\$$$$$$  |                \$$$$$$$ |\$$$$$$$\    \$  /   
 \_______|\__|  \__|   \____/  \______/ $$$$$$\ $$$$$$\  \_______| \_______|    \_/    
                                        \______|\______|                               
                                                                                       
                                                                                      """)
def print_tab() :
    tab_game_virgin = " __"+tab_position_possible[0]+"__|__"+tab_position_possible[1]+"__|__"+tab_position_possible[2]+"__"+"\n _____|_____|______ \n"+" __"+tab_position_possible[3]+"__|__"+tab_position_possible[4]+"__|__"+tab_position_possible[5]+"__"+"\n _____|_____|______\n"+" __"+tab_position_possible[6]+"__|__"+tab_position_possible[7]+"__|__"+tab_position_possible[8]+"__"    
    print(tab_game_virgin )

# variable de base importante 
tab_position_possible = [" " ," "," "," " ," " , " ", " ", " "," " ]
tab_game_virgin = " __"+tab_position_possible[0]+"__|__"+tab_position_possible[1]+"__|__"+tab_position_possible[2]+"__"+"\n _____|_____|______ \n"+" __"+tab_position_possible[3]+"__|__"+tab_position_possible[4]+"__|__"+tab_position_possible[5]+"__"+"\n _____|_____|______\n"+" __"+tab_position_possible[6]+"__|__"+tab_position_possible[7]+"__|__"+tab_position_possible[8]+"__"

# choix de la couleur 
choice_user_color = str(input("Choice the X or O for the game : "))

    
#########################################################################  game ################################################

#while choice_user_color == "O" or choice_user_color == "X" :
start_game = False
while start_game != True :
    if choice_user_color == "O" :
      choice_machine_color = "X"
      print("The choice of machine is : "+ choice_machine_color)
      game_main(choice_machine_color, choice_user_color, tab_position_possible )
      start_game = True
    elif choice_user_color == "X" :
        choice_machine_color = "O"
        print("The choice of machine is : "+ choice_machine_color)
        game_main(choice_machine_color, choice_user_color, tab_position_possible)
        start_game = True
    else :
        choice_user_color = input("Choice the X or O for the game (to CAPSLOCK): ")
        start_game = False
    
