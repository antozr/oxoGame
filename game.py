# Création d'un jeu de oxo avec la machine 


from random import randint
import time

print("""
                            $$\                                     $$\                      \n
                      $$ |                                    $$ |                     \n
 $$$$$$\  $$$$$$$\  $$$$$$\    $$$$$$\                   $$$$$$$ | $$$$$$\  $$\    $$\ \n
 \____$$\ $$  __$$\ \_$$  _|  $$  __$$\                 $$  __$$ |$$  __$$\ \$$\  $$  |\n
 $$$$$$$ |$$ |  $$ |  $$ |    $$ /  $$ |                $$ /  $$ |$$$$$$$$ | \$$\$$  / \n
$$  __$$ |$$ |  $$ |  $$ |$$\ $$ |  $$ |                $$ |  $$ |$$   ____|  \$$$  /  \n
\$$$$$$$ |$$ |  $$ |  \$$$$  |\$$$$$$  |                \$$$$$$$ |\$$$$$$$\    \$  /   \n
 \_______|\__|  \__|   \____/  \______/ $$$$$$\ $$$$$$\  \_______| \_______|    \_/    \n
                                        \______|\______|                               \n
                                                                                       \n
                                                                                      """)


# variable de base importante 
tab_position_possible = [" " ," "," "," " ," " , " ", " ", " "," " ]
tab_game_virgin = " __"+tab_position_possible[0]+"__|__"+tab_position_possible[1]+"__|__"+tab_position_possible[2]+"__"+"\n _____|_____|______ \n"+" __"+tab_position_possible[3]+"__|__"+tab_position_possible[4]+"__|__"+tab_position_possible[5]+"__"+"\n _____|_____|______\n"+" __"+tab_position_possible[6]+"__|__"+tab_position_possible[7]+"__|__"+tab_position_possible[8]+"__"


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
count_round = 0
choice_user = int(input('Choice your position between the disponibility number : '))
print("Your position is {}".format(choice_user))



if count_round == 0 :
    if choice_user >= 1 and choice_user <=9:
        tab_position_possible[choice_user] = choice_user_color
        #print(tab_position_possible[choice_user])
        time.sleep(0.2)
        choice_machine = randint(0,8)
        if choice_machine == choice_user :
            choice_machine = randint(0,8)
        print('The position of the machine is : {} '.format(choice_machine + 1))
        tab_position_possible[choice_machine] = choice_machine_color
        count_round += 1
        print(count_round)
    else : 
        print('The position dispinible is : '+len(tab_position_possible))
        choice_user = int(input('Choice your position between the disponibility number : '))
else : 
    print('You past the second round !!!!')
    
#création du tableau à chaque tours 
tab_game_virgin = " __"+tab_position_possible[0]+"__|__"+tab_position_possible[1]+"__|__"+tab_position_possible[2]+"__"+"\n _____|_____|______ \n"+" __"+tab_position_possible[3]+"__|__"+tab_position_possible[4]+"__|__"+tab_position_possible[5]+"__"+"\n _____|_____|______\n"+" __"+tab_position_possible[6]+"__|__"+tab_position_possible[7]+"__|__"+tab_position_possible[8]+"__"    
print(tab_game_virgin )