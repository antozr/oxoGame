from random import randint

def verification_analyse_causality (new_choice, choice_user): #choice user 
    #print(new_choice)
    if choice_user in new_choice[0:2] :
        #print(new_choice)
        new_choice_machine = new_choice[3:6]##### faire une vérifivation et sortir un nombre de ce tablea u
        new_choice_machine = new_choice_machine[randint(0, len(new_choice_machine)-1)]
        # print(new_choice_machine)
        # print('hio1')
        return new_choice_machine
    elif choice_user in new_choice[2:4] :
        #print(new_choice)
        new_choice_machine = new_choice[0:2] or new_choice[4:6]
        new_choice_machine = new_choice_machine[randint(0, len(new_choice_machine)-1)]
        # print(new_choice_machine)
        # print('hio2')
        return new_choice_machine
    elif len(new_choice) == 6 :
        #print(new_choice)
        if choice_user in new_choice[4:6] :
             new_choice_machine = new_choice[:4]
             new_choice_machine = new_choice_machine[randint(0, len(new_choice_machine)-1)]
             #print(new_choice_machine)
             #print('hio3')
             return new_choice_machine
    else : 
        new_choice_machine = new_choice[randint(0, len(new_choice) - 1)]
        #print(new_choice_machine)
        #print('hio4')
        return new_choice_machine
        
        ## vérifier utilité et var 