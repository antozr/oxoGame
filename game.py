# Création d'un jeu de oxo avec la machine 


from random import randint
import time
from verification_analyse import verification_analyse_causality
from choice_machine import verification_choice_machine

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


# variable de base importante 
tab_position_possible = [" " ," "," "," " ," " , " ", " ", " "," " ]
tab_game_virgin = " __"+tab_position_possible[0]+"__|__"+tab_position_possible[1]+"__|__"+tab_position_possible[2]+"__"+"\n _____|_____|______ \n"+" __"+tab_position_possible[3]+"__|__"+tab_position_possible[4]+"__|__"+tab_position_possible[5]+"__"+"\n _____|_____|______\n"+" __"+tab_position_possible[6]+"__|__"+tab_position_possible[7]+"__|__"+tab_position_possible[8]+"__"

# choice_user = int(input('Choice your position between the disponibility number : '))
# print(choice_user)
#new_choice = [1, 2, 5, 6, 7, 9]
# print(new_choice[:-2])
# size_list = len(new_choice)-1
# print(size_list)
# #new_choice = new_choice[randint(0,len(new_choice)-1)]
# new_choice_machine = verification_analyse_causality(new_choice, choice_user)
# print(new_choice_machine)
# new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
# print(new_choice)


# choix de la couleur 
choice_user_color = str(input("Choice the X or O for the game : "))

if choice_user_color == "O" :
      choice_machine_color = "X"
elif choice_user_color == "X" :
    choice_machine_color = "O"
else :
    choice_user_color = input("Choice the X or O for the game (to CAPSLOCK): ")
    
    
print("The choice of machine is : "+ choice_machine_color)

#choix de la position 
# print(len(tab_position_possible))
finish_game = False
count_round = 0
print('Your possibility is between 1 and 9 \n')
choice_user = int(input('Choice your position between the disponibility number : '))
print("Your position is {}".format(choice_user))

### création de la fonction pour le jeu 

### vérification pour ''' l'ia ''' du robot 
# def verification_choice_machine (choice_machine, choice_user):
    
#     if choice_machine == 1 :
#         new_choice = [2, 3, 4, 5, 7, 9]
#         new_choice_machine = verification_analyse_causality(new_choice,choice_user)
#         size_list = len(new_choice)-1
#         #new_choice = new_choice[randint(0,len(new_choice)-1)]
#         new_choice_machine = verification_analyse_causality(new_choice,choice_user)
#         new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
#         if new_choice == choice_user :
#             new_choice = new_choice[randint(0,size_list)]
#         return new_choice
    
#     elif choice_machine == 2 :
#         new_choice = [1, 3, 5, 8]
        
#         size_list = len(new_choice)-1
#         #new_choice = new_choice[randint(0,len(new_choice)-1)]
#         new_choice_machine = verification_analyse_causality(new_choice,choice_user)
#         new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
#         if new_choice == choice_user :
#             new_choice = new_choice[randint(0,size_list)]
#         return new_choice
#     elif choice_machine == 3 :
#         new_choice = [1, 2, 5, 6, 7, 9]
#         size_list = len(new_choice)-1
#         #new_choice = new_choice[randint(0,len(new_choice)-1)]
#         new_choice_machine = verification_analyse_causality(new_choice,choice_user)
#         new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
#         if new_choice == choice_user :
#             new_choice = new_choice[randint(0,size_list)]
#         return new_choice
    
#     elif choice_machine == 4 :
#         new_choice = [1, 5, 6, 7]
#         size_list = len(new_choice)-1
#         #new_choice = new_choice[randint(0,len(new_choice)-1)]
#         new_choice_machine = verification_analyse_causality(new_choice,choice_user)
#         new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
#         if new_choice == choice_user :
#             new_choice = new_choice[randint(0,size_list)]
#         return new_choice
    
#     elif choice_machine == 5 :
#         new_choice = [2, 4, 6, 8]
#         #new_choice = new_choice[randint(0,len(new_choice)-1)]
#         size_list = len(new_choice)-1
#         #new_choice = new_choice[randint(0,len(new_choice)-1)]
#         new_choice_machine = verification_analyse_causality(new_choice,choice_user)
#         size_choice_machine =  len(new_choice_machine) - 1
#         print(new_choice_machine)
#         new_choice = new_choice_machine[randint(0, size_choice_machine)]
#         if new_choice == choice_user :
#             new_choice = new_choice[randint(0,size_list)]
#         return new_choice
    
#     elif choice_machine == 6 :
#         new_choice = [3, 4, 7, 9]
#         #new_choice = new_choice[randint(0,len(new_choice)-1)]
#         size_list = len(new_choice)-1
#         #new_choice = new_choice[randint(0,len(new_choice)-1)]
#         new_choice_machine = verification_analyse_causality(new_choice,choice_user)
#         size_choice_machine =  len(new_choice_machine) - 1
        
#         new_choice = new_choice_machine[randint(0,size_choice_machine)]
#         if new_choice == choice_user :
#             new_choice = new_choice[randint(0,size_list)]
#         return new_choice
    
#     elif choice_machine == 7 :
#         new_choice = [1, 3, 4, 5,8, 9]
#         #new_choice = new_choice[randint(0,len(new_choice)-1)]
#         size_list = len(new_choice)-1
#         #new_choice = new_choice[randint(0,len(new_choice)-1)]
#         new_choice_machine = verification_analyse_causality(new_choice,choice_user)
#         new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
#         if new_choice == choice_user :
#             new_choice = new_choice[randint(0,size_list)]
#         return new_choice
    
#     elif choice_machine == 8 :
#         new_choice = [2, 5,7, 9]
#         #new_choice = new_choice[randint(0,len(new_choice)-1)]
#         size_list = len(new_choice)-1
#         #new_choice = new_choice[randint(0,len(new_choice)-1)]
#         new_choice_machine = verification_analyse_causality(new_choice, choice_user)
#         new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
#         if new_choice == choice_user :
#             new_choice = new_choice[randint(0,size_list)]
#         return new_choice
    
#     elif choice_machine == 9 :
#         new_choice = [1, 3, 5, 6, 7, 8]
#         size_list = len(new_choice)-1
#         #new_choice = new_choice[randint(0,len(new_choice)-1)]
#         new_choice_machine = verification_analyse_causality(new_choice, choice_user)
#         new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
#         if new_choice == choice_user :
#             new_choice = new_choice[randint(0,size_list)]
#         return new_choice
    
#########################################################################  game 
while finish_game != True:
    if count_round == 0 :
        if choice_user >= 1 and choice_user <=9:
            tab_position_possible[choice_user - 1] = choice_user_color
            print(tab_position_possible[choice_user-1]) # vérification de la position problème avec la position 0/1
            #machine time 
            time.sleep(0.2)
            choice_machine = randint(0,8)
            if choice_machine == choice_user :
                choice_machine = randint(0,8)
            print('The position of the machine is : {} '.format(choice_machine + 1))
            tab_position_possible[choice_machine] = choice_machine_color
            count_round += 1
            print(count_round)
            ##
            #création du tableau à chaque tours 
            tab_game_virgin = " __"+tab_position_possible[0]+"__|__"+tab_position_possible[1]+"__|__"+tab_position_possible[2]+"__"+"\n _____|_____|______ \n"+" __"+tab_position_possible[3]+"__|__"+tab_position_possible[4]+"__|__"+tab_position_possible[5]+"__"+"\n _____|_____|______\n"+" __"+tab_position_possible[6]+"__|__"+tab_position_possible[7]+"__|__"+tab_position_possible[8]+"__"    
            print(tab_game_virgin )
        else : 
            print('The position dispinible is : '+len(tab_position_possible))
            choice_user = int(input('Choice your position between the disponibility number : '))
            
    elif count_round >= 1 : 
        choice_user = int(input('Choice your position between the disponibility number : '))
        if choice_user >= 1 and choice_user <=9:
            #verification_choice_machine ()
            tab_position_possible[choice_user - 1] = choice_user_color
            #print(tab_position_possible[choice_user])
            #machine time 
            time.sleep(0.2)
            # choice_machine = randint(0,8)
            # if choice_machine == choice_user :
            choice_machine = randint(0,8)
            choice_machine = 6
            choice_machine = verification_choice_machine (choice_machine, choice_user)
            print(choice_machine)
            print('The position of the machine is : {} '.format(choice_machine))
            tab_position_possible[choice_machine-1] = choice_machine_color
            #change round 
            count_round += 1
            print(count_round)
            ##
            #création du tableau à chaque tours 
            tab_game_virgin = " __"+tab_position_possible[0]+"__|__"+tab_position_possible[1]+"__|__"+tab_position_possible[2]+"__"+"\n _____|_____|______ \n"+" __"+tab_position_possible[3]+"__|__"+tab_position_possible[4]+"__|__"+tab_position_possible[5]+"__"+"\n _____|_____|______\n"+" __"+tab_position_possible[6]+"__|__"+tab_position_possible[7]+"__|__"+tab_position_possible[8]+"__"    
            print(tab_game_virgin )
        else : 
            print('The position dispinible is : '+len(tab_position_possible))
            choice_user = int(input('Choice your position between the disponibility number : '))
    else : 
        print('You past the second round !!!!')
        finish_game = True

# #création du tableau à chaque tours 
# tab_game_virgin = " __"+tab_position_possible[0]+"__|__"+tab_position_possible[1]+"__|__"+tab_position_possible[2]+"__"+"\n _____|_____|______ \n"+" __"+tab_position_possible[3]+"__|__"+tab_position_possible[4]+"__|__"+tab_position_possible[5]+"__"+"\n _____|_____|______\n"+" __"+tab_position_possible[6]+"__|__"+tab_position_possible[7]+"__|__"+tab_position_possible[8]+"__"    
# print(tab_game_virgin )