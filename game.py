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
# def game_main(choice_machine_color, choice_user_color):
#     finish_game = False
#     count_round = 0
    
    
#     while finish_game == False:
#         # print(finish_game)
#         # print('cest fini ????????????????')
#         if count_round == 0 :
#             print('Your possibility is between 1 and 9 \n')
#             choice_user = int(input('Choice your position between the disponibility number : '))
#             print("Your position is {}".format(choice_user))
#             if choice_user >= 1 and choice_user <=9:
#                 tab_position_possible[choice_user - 1] = choice_user_color
#                 #machine time 
#                 time.sleep(0.2)
#                 choice_machine = randint(0,8)
#                 if choice_machine == choice_user :
#                     choice_machine = randint(0,8)
#                 print('The position of the machine is : {} '.format(choice_machine + 1))
#                 tab_position_possible[choice_machine] = choice_machine_color
#                 count_round += 1
#                 #création du tableau à chaque tours 
#                 print_tab()
#             else : 
#                 print('The position dispinible is : '+len(tab_position_possible))
#                 choice_user = int(input('Choice your position between the disponibility number : '))
                
#         elif count_round == 4 :
#             print('The game is end !!! \n The winner is ... ')
#             finish_game = winner (choice_machine_color,tab_position_possible, choice_user_color , print_tab)
#             print(finish_game)
#             finish_game == True
#             count_round == 4
           
#         elif count_round == 3:
#             # en attendant end
#             finish_game = winner (choice_machine_color,tab_position_possible, choice_user_color , print_tab)
#             print(finish_game)
#             if finish_game == True :
#                 print('YES THE GAME IS FINISH')
#                 count_round == 3
#             else :
#                 choice_user = int(input('Choice your position between the disponibility number : '))
#             if choice_user >= 1 and choice_user <=9:
#                 tab_position_possible[choice_user - 1] = choice_user_color
#                 #machine time 
#                 time.sleep(0.2)
#                 choice_machine = randint(0,8)
#                 print('geoo end round')
#                 if choice_machine == None :
#                      choice_machine = randint(0,8)
#                 if choice_machine == None :
#                     choice_machine = verification_choice_machine (choice_machine, choice_user)
                
#                 print('geoo2')
#                 print(choice_machine)
#                 print('The position of the machine is : {} '.format(choice_machine))
#                 tab_position_possible[choice_machine-1] = choice_machine_color
#                 #change round 
#                 count_round == 4
#                 print("We are in second round.{}".format(count_round))
#                 print(count_round)
#                 print('tourn numéro')
#                 #création du tableau à chaque tours 
#                 print_tab()
#                 print(tab_position_possible[0:3])
#                 print(tab_position_possible)
#             else : 
#                 print('The position dispinible is : '+len(tab_position_possible))
#                 choice_user = int(input('Choice your position between the disponibility number : '))
                
            
#         elif count_round == 2 : 
#             choice_user = int(input('Choice your position between the disponibility number : '))
#             if choice_user >= 1 and choice_user <=9:
#                 tab_position_possible[choice_user - 1] = choice_user_color
#                 #machine time 
#                 time.sleep(0.2)
#                 choice_machine = randint(0,8)
#                 print('geoo')
#                 if choice_machine == None :
#                      choice_machine = randint(0,8)
#                 if choice_machine == None :
#                     choice_machine = verification_choice_machine (choice_machine, choice_user)
                
#                 print('geoo2')
#                 print(choice_machine)
#                 print('The position of the machine is : {} '.format(choice_machine))
#                 tab_position_possible[choice_machine-1] = choice_machine_color
#                 #change round 
#                 count_round += 1
#                 print("We are in second round.{}".format(count_round))
#                 print(count_round)
#                 print('tourn numéro')
#                 #création du tableau à chaque tours 
#                 print_tab()
#                 print(tab_position_possible[0:3])
#                 print(tab_position_possible)
#             else : 
#                 print('The position dispinible is : '+len(tab_position_possible))
#                 choice_user = int(input('Choice your position between the disponibility number : '))
                     
#         elif count_round == 1 : 
#             choice_user = int(input('Choice your position between the disponibility number : '))
#             if choice_user >= 1 and choice_user <=9:
#                 tab_position_possible[choice_user - 1] = choice_user_color
#                 #machine time 
#                 time.sleep(0.2)
#                 choice_machine = randint(0,8)
#                 print(choice_machine)
#                 print('geoo')
#                 choice_machine = verification_choice_machine (choice_machine, choice_user)
#                 print('geoo2')
#                 print(choice_machine)
#                 print('The position of the machine is : {} '.format(choice_machine))
#                 tab_position_possible[choice_machine-1] = choice_machine_color
#                 #change round 
#                 count_round += 1
#                 print("We are in second round.")
#                 print(count_round)
#                 print('tourn numéro')
#                 #création du tableau à chaque tours 
#                 print_tab()
                
#             else : 
#                 print('The position dispinible is : '+len(tab_position_possible))
#                 choice_user = int(input('Choice your position between the disponibility number : '))
        
#         else : 
#             print("Restart the game. ")
#             finish_game = True





#while choice_user_color == "O" or choice_user_color == "X" :
start_game = False
while start_game != True :
    if choice_user_color == "O" :
      choice_machine_color = "X"
      print("The choice of machine is : "+ choice_machine_color)
    #   game_main(choice_machine_color, choice_user_color)
      game_main(choice_machine_color, choice_user_color, tab_position_possible )
      start_game = True
    #   game_main (choice_user_color, choice_machine_color)
    elif choice_user_color == "X" :
        choice_machine_color = "O"
        print("The choice of machine is : "+ choice_machine_color)
        game_main(choice_machine_color, choice_user_color, tab_position_possible)
        #game_main(choice_machine_color, choice_user_color)
        start_game = True
        # game_main (choice_user_color, choice_machine_color)
    else :
        choice_user_color = input("Choice the X or O for the game (to CAPSLOCK): ")
        start_game = False
    
