from verification_analyse import verification_analyse_causality
from random import randint

def verification_choice_machine (choice_machine, choice_user):
    print("choix machine {}".format(choice_machine))
    if choice_machine == 1 :
        new_choice = [2, 3, 4, 5, 7, 9]
        new_choice_machine = verification_analyse_causality(new_choice,choice_user)
        size_list = len(new_choice)-1
        #new_choice = new_choice[randint(0,len(new_choice)-1)]
        new_choice_machine = verification_analyse_causality(new_choice,choice_user)
        new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
        if new_choice == choice_user :
            new_choice = new_choice[randint(0,size_list)]
        return new_choice
    
    elif choice_machine == 2 :
        new_choice = [1, 3, 5, 8]
        
        size_list = len(new_choice)-1
        #new_choice = new_choice[randint(0,len(new_choice)-1)]
        new_choice_machine = verification_analyse_causality(new_choice,choice_user)
        new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
        if new_choice == choice_user :
            new_choice = new_choice[randint(0,size_list)]
        return new_choice
    elif choice_machine == 3 :
        new_choice = [1, 2, 5, 6, 7, 9]
        size_list = len(new_choice)-1
        #new_choice = new_choice[randint(0,len(new_choice)-1)]
        new_choice_machine = verification_analyse_causality(new_choice,choice_user)
        new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
        if new_choice == choice_user :
            new_choice = new_choice[randint(0,size_list)]
        return new_choice
    
    elif choice_machine == 4 :
        new_choice = [1, 5, 6, 7]
        size_list = len(new_choice)-1
        #new_choice = new_choice[randint(0,len(new_choice)-1)]
        new_choice_machine = verification_analyse_causality(new_choice,choice_user)
        new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
        if new_choice == choice_user :
            new_choice = new_choice[randint(0,size_list)]
        return new_choice
    
    elif choice_machine == 5 :
        new_choice = [2, 4, 6, 8]
        #new_choice = new_choice[randint(0,len(new_choice)-1)]
        size_list = len(new_choice)-1
        #new_choice = new_choice[randint(0,len(new_choice)-1)]
        new_choice_machine = verification_analyse_causality(new_choice,choice_user)
        new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
        if new_choice == choice_user :
            new_choice = new_choice[randint(0,size_list)]
        return new_choice
    
    elif choice_machine == 6 :
        new_choice = [3, 4, 7, 9]
        size_list = len(new_choice)-1
        new_choice_machine = verification_analyse_causality(new_choice,choice_user)
        new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
        if new_choice == choice_user :
            new_choice = new_choice[randint(0,size_list)]
        return new_choice
    
    elif choice_machine == 7 :
        new_choice = [1, 3, 4, 5,8, 9]
        #new_choice = new_choice[randint(0,len(new_choice)-1)]
        size_list = len(new_choice)-1
        #new_choice = new_choice[randint(0,len(new_choice)-1)]
        new_choice_machine = verification_analyse_causality(new_choice,choice_user)
        new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
        if new_choice == choice_user :
            new_choice = new_choice[randint(0,size_list)]
        return new_choice
    
    elif choice_machine == 8 :
        new_choice = [2, 5,7, 9]
        #new_choice = new_choice[randint(0,len(new_choice)-1)]
        size_list = len(new_choice)-1
        #new_choice = new_choice[randint(0,len(new_choice)-1)]
        new_choice_machine = verification_analyse_causality(new_choice, choice_user)
        new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
        if new_choice == choice_user :
            new_choice = new_choice[randint(0,size_list)]
        return new_choice
    
    elif choice_machine == 9 :
        new_choice = [1, 3, 5, 6, 7, 8]
        size_list = len(new_choice)-1
        #new_choice = new_choice[randint(0,len(new_choice)-1)]
        new_choice_machine = verification_analyse_causality(new_choice, choice_user)
        new_choice = new_choice_machine[randint(0, len(new_choice_machine) - 1)]
        if new_choice == choice_user :
            new_choice = new_choice[randint(0,size_list)]
        return new_choice
    