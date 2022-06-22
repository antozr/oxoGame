import time
from random import randint
from choice_machine import verification_choice_machine




def game_main (choice_user_color, choice_machine_color):
    def print_tab() :
        tab_game_virgin = " __"+tab_position_possible[0]+"__|__"+tab_position_possible[1]+"__|__"+tab_position_possible[2]+"__"+"\n _____|_____|______ \n"+" __"+tab_position_possible[3]+"__|__"+tab_position_possible[4]+"__|__"+tab_position_possible[5]+"__"+"\n _____|_____|______\n"+" __"+tab_position_possible[6]+"__|__"+tab_position_possible[7]+"__|__"+tab_position_possible[8]+"__"    
        print(tab_game_virgin )
    #choix de la position 
    # print(len(tab_position_possible))
    # variable de base importante 
    tab_position_possible = [" " ," "," "," " ," " , " ", " ", " "," " ]
    tab_game_virgin = " __"+tab_position_possible[0]+"__|__"+tab_position_possible[1]+"__|__"+tab_position_possible[2]+"__"+"\n _____|_____|______ \n"+" __"+tab_position_possible[3]+"__|__"+tab_position_possible[4]+"__|__"+tab_position_possible[5]+"__"+"\n _____|_____|______\n"+" __"+tab_position_possible[6]+"__|__"+tab_position_possible[7]+"__|__"+tab_position_possible[8]+"__"

    finish_game = False
    count_round = 0
    print('Your possibility is between 1 and 9 \n')
    choice_user = int(input('Choice your position between the disponibility number : '))
    print("Your position is {}".format(choice_user))

    while finish_game != True:
        if count_round == 0 :
            if choice_user >= 1 and choice_user <=9:
                tab_position_possible[choice_user - 1] = choice_user_color
                print(tab_position_possible[choice_user-1]) 
                #machine time 
                time.sleep(0.2)
                choice_machine = randint(0,8)
                if choice_machine == choice_user :
                    choice_machine = randint(0,8)
                print('The position of the machine is : {} '.format(choice_machine + 1))
                tab_position_possible[choice_machine] = choice_machine_color
                count_round += 1
                print(count_round)
                #création du tableau à chaque tours 
                print_tab()
            else : 
                print('The position dispinible is : '+len(tab_position_possible))
                choice_user = int(input('Choice your position between the disponibility number : '))
                
        elif count_round == 4 :
            print('The game is end !!! \n The winner is ... ')
            print_tab()
            finish_game = True
                
        elif count_round >= 1 : 
            choice_user = int(input('Choice your position between the disponibility number : '))
            if choice_user >= 1 and choice_user <=9:
                tab_position_possible[choice_user - 1] = choice_user_color
                #machine time 
                time.sleep(0.2)
                choice_machine = randint(0,8)
                choice_machine = 6
                choice_machine = verification_choice_machine (choice_machine, choice_user)
                print(choice_machine)
                print('The position of the machine is : {} '.format(choice_machine))
                tab_position_possible[choice_machine-1] = choice_machine_color
                #change round 
                count_round += 1
                print("We are in second round.")
                #création du tableau à chaque tours 
                print_tab()
                
            else : 
                print('The position dispinible is : '+len(tab_position_possible))
                choice_user = int(input('Choice your position between the disponibility number : '))
        
        else : 
            print("Restart the game. ")
            finish_game = True
