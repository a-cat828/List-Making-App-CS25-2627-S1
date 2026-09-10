favort = []
exitt = False
numb= 0
while not exitt:
    is_where_inportan = input("do you care where it is in the list? (y/n)")
    reassign_yes_or_no = input("do you whant to reassign one of your favorite movie?/shows?(y/n)")
    remove_yes_or_no = input("do you want to remove one of your favorite movie?/shows?(y/n)")
    
    if is_where_inportan == "y":
         where= int(input("enter where in the list?(number)"))
         thing_add_to_list = input("what is one of your favorite movie/shows?(say exit to exit)")
         if thing_add_to_list == "exit":
             exitt = True
         else:
            where= where - 1
            favort.insert(where,thing_add_to_list)
            for i in favort:
                 print(favort[numb], numb + 1)
                 numb = numb + 1
            numb = 0
    elif reassign_yes_or_no == "y":
        where = int(input("enter where in the list?(number)"))
        to_make_into = input("what do you want to reassign to?(say exit to exit)")
        if to_make_into == "exit":
            exitt = True
        else:
            where = where - 1
            favort[where]= to_make_into
            for i in favort:
                print(favort[numb], numb + 1)
                numb = numb + 1
            numb = 0
    elif remove_yes_or_no == "y":
        where = int(input("enter what in the list you want to remove?(number)"))
        where = where - 1
        favort.pop(where)
        for i in favort:
            print(favort[numb], numb + 1)
            numb = numb + 1
        numb = 0
    elif is_where_inportan == "n" and reassign_yes_or_no == "n" :
        thing_add_to_list = input("what is one of your favorite movie/shows?(say exit to exit)")
        if thing_add_to_list == "exit":
            exitt = True
        else:
            favort.append(thing_add_to_list)
            for i in favort:
                print(favort[numb], numb + 1)
                numb=numb+1
            numb = 0