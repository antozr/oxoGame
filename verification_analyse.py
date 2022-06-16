from random import randint

def verification_analyse_causality (new_choice, choice_user): #choice user 
    print(new_choice)
    if choice_user in new_choice[0:2] :
        new_choice_machine = new_choice[:-4]
        return new_choice_machine
    elif choice_user in new_choice[2:4] :
        new_choice_machine = new_choice[0:1] or new_choice[4:5]
        return new_choice_machine
    elif len(new_choice) == 6 :
        if choice_user in new_choice[4:6] :
             new_choice_machine = new_choice[:4]
             return new_choice_machine
    else : 
        new_choice_machine = new_choice[randint(0, len(new_choice) - 1)]
        return new_choice_machine
        
        ## vérifier utilité et var 