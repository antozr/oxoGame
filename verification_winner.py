
from tab_print import print_tab



def function_winner (tab_position_possible, winner):
    print(tab_position_possible)
    finish_game = True
    if winner == "machine" :
        winner_tag = "la machine"
    else :
        winner_tag = "toi"
    print("C'est {} qui a gagné!!! \n".format(winner_tag))
    print_tab(tab_position_possible)
    return finish_game

def winner (choice_machine_color,tab_position_possible, choice_user_color , print_tab) :
    if choice_machine_color in  tab_position_possible[0] and choice_machine_color in  tab_position_possible[1] and choice_machine_color in  tab_position_possible[2]:
        finish_game = function_winner(tab_position_possible, "machine")
        return finish_game
    
    elif  choice_user_color in  tab_position_possible[0] and choice_user_color in  tab_position_possible[1] and choice_user_color in  tab_position_possible[2] :
        finish_game = function_winner(tab_position_possible, "toi")
        return finish_game
    
    elif choice_machine_color in  tab_position_possible[3] and choice_machine_color in  tab_position_possible[4] and choice_machine_color in  tab_position_possible[6] :
        finish_game = function_winner(tab_position_possible, "machine")
        return finish_game

    elif choice_user_color  in  tab_position_possible[3] and choice_user_color in  tab_position_possible[4] and choice_user_color in  tab_position_possible[6] :
        finish_game = function_winner(tab_position_possible, "toi")
        return finish_game
    
    elif choice_machine_color in  tab_position_possible[6] and choice_machine_color in  tab_position_possible[7] and choice_machine_color in  tab_position_possible[8] :
        finish_game = function_winner(tab_position_possible, "machine")
        return finish_game
    
    elif choice_user_color in   tab_position_possible[6] and choice_user_color in  tab_position_possible[7] and choice_user_color in  tab_position_possible[8] :
        finish_game = function_winner(tab_position_possible, "toi")
        return finish_game
    
    elif choice_machine_color in tab_position_possible[0] and choice_machine_color in  tab_position_possible[3] and choice_machine_color in  tab_position_possible[6]  :
        finish_game = function_winner(tab_position_possible, "machine")
        return finish_game
    
    elif choice_user_color in  tab_position_possible[0] and choice_user_color in  tab_position_possible[3] and choice_user_color in  tab_position_possible[6] :
        finish_game = function_winner(tab_position_possible, "toi")
        return finish_game
    
    elif choice_machine_color in tab_position_possible[1] and choice_machine_color in  tab_position_possible[4] and choice_machine_color in  tab_position_possible[7]  :
        finish_game = function_winner(tab_position_possible, "machine")
        return finish_game
    
    elif choice_user_color in tab_position_possible[1] and choice_user_color in  tab_position_possible[4] and choice_user_color in  tab_position_possible[7] :
        finish_game = function_winner(tab_position_possible, "toi")
        return finish_game
    
    elif choice_machine_color in tab_position_possible[2] and choice_machine_color in  tab_position_possible[5] and choice_machine_color in  tab_position_possible[8]  :
        finish_game = function_winner(tab_position_possible, "machine")
        return finish_game
    
    elif choice_user_color in  tab_position_possible[2] and choice_user_color in  tab_position_possible[5] and choice_user_color in  tab_position_possible[8] :
        finish_game = function_winner(tab_position_possible, "toi")
        return finish_game
    
    elif choice_machine_color in tab_position_possible[0] and choice_machine_color in  tab_position_possible[4] and choice_machine_color in  tab_position_possible[8]  :
        finish_game = function_winner(tab_position_possible, "machine")
        return finish_game
    elif choice_user_color in  tab_position_possible[0] and choice_user_color in  tab_position_possible[4] and choice_user_color in  tab_position_possible[8] :
        finish_game = function_winner(tab_position_possible, "toi")
        return finish_game
    elif choice_machine_color in tab_position_possible[2] and choice_machine_color in  tab_position_possible[4] and choice_machine_color in  tab_position_possible[6]  :
        finish_game = function_winner(tab_position_possible, "machine")
        return finish_game
    elif choice_user_color in  tab_position_possible[2] and choice_user_color in  tab_position_possible[4] and choice_user_color in  tab_position_possible[6] :
        finish_game = function_winner(tab_position_possible, "toi")
        return finish_game
    else :
        print('C\'est pas encore fini')