import time
from random import randint
from choice_machine import verification_choice_machine
from tab_print import print_tab
from verification_winner import winner



def game_main(choice_machine_color, choice_user_color, tab_position_possible ):
    finish_game = False
    count_round = 0
    
    
    while finish_game == False:
        if count_round == 0 :
            print('Your possibility is between 1 and 9 \n')
            choice_user = int(input('Choice your position between the disponibility number : '))
            print("Your position is {}".format(choice_user))
            if choice_user >= 1 and choice_user <=9:
                tab_position_possible[choice_user - 1] = choice_user_color
                #machine time 
                time.sleep(0.2)
                choice_machine = randint(0,8)
                if choice_machine == choice_user :
                    choice_machine = randint(0,8)
                print('The position of the machine is : {} '.format(choice_machine + 1))
                tab_position_possible[choice_machine] = choice_machine_color
                count_round += 1
                #création du tableau à chaque tours 
                print_tab(tab_position_possible)
            else : 
                print('The position dispinible is : '+len(tab_position_possible))
                choice_user = int(input('Choice your position between the disponibility number : '))
                
        elif count_round == 4 :
            print('The game is end !!! \n The winner is ... ')
            finish_game = winner (choice_machine_color,tab_position_possible, choice_user_color , print_tab,count_round)
            print(finish_game)
            finish_game == True
            count_round == 4
           
        elif count_round == 3:
            # en attendant end
            finish_game = winner (choice_machine_color,tab_position_possible, choice_user_color , print_tab,count_round)
            print(finish_game)
            if finish_game == True :
                print('YES THE GAME IS FINISH')
                count_round == 3
            else :
                choice_user = int(input('Choice your position between the disponibility number : '))
                if choice_user >= 1 and choice_user <=9:
                    tab_position_possible[choice_user - 1] = choice_user_color
                    #machine time 
                    time.sleep(0.2)
                    choice_machine = randint(0,8)
                    if choice_machine == None :
                        choice_machine = randint(0,8)
                    if choice_machine == None :
                        choice_machine = verification_choice_machine (choice_machine, choice_user)
                    if choice_machine == choice_user :
                        choice_machine = randint(0,8)
                        choice_machine = verification_choice_machine (choice_machine, choice_user)
                        if choice_machine == None :
                            choice_machine = randint(0,8)
                        if choice_machine == None :
                            choice_machine = verification_choice_machine (choice_machine, choice_user)
                    print('The position of the machine is : {} '.format(choice_machine))
                    tab_position_possible[choice_machine-1] = choice_machine_color
                    #change round 
                    count_round == 4
                    print("We are in second round.{}".format(count_round))
                    #création du tableau à chaque tours 
                    print_tab(tab_position_possible)
                    # print(tab_position_possible[0:3])
                    # print(tab_position_possible)
                else : 
                    print('The position dispinible is : '+len(tab_position_possible))
                    choice_user = int(input('Choice your position between the disponibility number : '))
                
            
        elif count_round == 2 : 
            choice_user = int(input('Choice your position between the disponibility number : '))
            if choice_user >= 1 and choice_user <=9:
                tab_position_possible[choice_user - 1] = choice_user_color
                #machine time 
                time.sleep(0.2)
                choice_machine = randint(0,8)
                if choice_machine == None :
                     choice_machine = randint(0,8)
                if choice_machine == None :
                    choice_machine = verification_choice_machine (choice_machine, choice_user)
                if choice_machine == choice_user :
                    choice_machine = randint(0,8)
                    choice_machine = verification_choice_machine (choice_machine, choice_user)
                    if choice_machine == None :
                     choice_machine = randint(0,8)
                    if choice_machine == None :
                        choice_machine = verification_choice_machine (choice_machine, choice_user)
                print('The position of the machine is : {} '.format(choice_machine))
                tab_position_possible[choice_machine-1] = choice_machine_color
                #change round 
                count_round += 1
                print("We are in second round.{}".format(count_round))
                #création du tableau à chaque tours 
                print_tab(tab_position_possible)
                # print(tab_position_possible[0:3])
                # print(tab_position_possible)
            else : 
                print('The position dispinible is : '+len(tab_position_possible))
                choice_user = int(input('Choice your position between the disponibility number : '))
                     
        elif count_round == 1 : 
            choice_user = int(input('Choice your position between the disponibility number : '))
            if choice_user >= 1 and choice_user <=9:
                tab_position_possible[choice_user - 1] = choice_user_color
                #machine time 
                time.sleep(0.2)
                choice_machine = randint(0,8)
                choice_machine = verification_choice_machine (choice_machine, choice_user)
                if choice_machine == choice_user :
                    choice_machine = randint(0,8)
                    choice_machine = verification_choice_machine (choice_machine, choice_user)
                print('The position of the machine is : {} '.format(choice_machine))
                tab_position_possible[choice_machine-1] = choice_machine_color
                #change round 
                count_round += 1
                print("We are in second round.")
                #création du tableau à chaque tours 
                print_tab(tab_position_possible)
                
            else : 
                print('The position dispinible is : '+len(tab_position_possible))
                choice_user = int(input('Choice your position between the disponibility number : '))
        
        else : 
            print("Restart the game. ")
            finish_game = True
