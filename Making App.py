favort = []
exitt = False
numb= 0
while not exitt:
    is_where_inportan = input("do you care where it is in the list? (y/n)")
    reassign_yes_or_no = input("do you whant to reassign one of your favorite movie?/shows?(y/n)")
    remove_yes_or_no = input("do you want to remove one of your favorite movie?/shows?(y/n)")
    check_yes_no = input("do you want to check if something is in the list?(y/n)")
    check_numb_of = input("what do you want to check how many are in the list?(y/n) ")
    if is_where_inportan == "y":
         where= int(input("enter where in the list?(number)"))
         thing_add_to_list = input("what is one of your favorite movie/shows?(say exit to exit)")
         if thing_add_to_list == "exit":
             exitt = True
         else:
            if where <= len(favort):
                where= where - 1
                favort.insert(where,thing_add_to_list)
            else:
                print("invalid input")
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
            if where <= len(favort):
                where = where - 1
                favort[where]= to_make_into
            else:
                print("invalid input")
            for i in favort:
                print(favort[numb], numb + 1)
                numb = numb + 1
            numb = 0
    elif remove_yes_or_no == "y":
        where = int(input("enter what in the list you want to remove?(number)"))
        where = where - 1
        if where <= len(favort):
            favort.pop(where)
        else:
            print("invalid input")
        for i in favort:
            print(favort[numb], numb + 1)
            numb = numb + 1
        numb = 0
    elif check_yes_no == "y":
        where = (input("what do you want to check if it is in the list?(say exit to exit) "))
        if where == "exit":
            exitt = True
        else:
            if where in favort:
                print("it is in the list")
            else:
                print("it is not in the list")
            for i in favort:
                print(favort[numb], numb + 1)
                numb=numb+1
            numb = 0
    elif check_numb_of == "y":
        print("there are", (len(favort)), "favorite movies/shows")
        for i in favort:
            print(favort[numb], numb + 1)
            numb = numb + 1
        numb = 0
    elif is_where_inportan == "n" and reassign_yes_or_no == "n" and remove_yes_or_no == "n" and check_yes_no == "n" and check_numb_of == "n":
        thing_add_to_list = input("what is one of your favorite movie/shows?(say exit to exit)")
        if thing_add_to_list == "exit":
            exitt = True
        else:
            favort.append(thing_add_to_list)
            for i in favort:
                print(favort[numb], numb + 1)
                numb=numb+1
            numb = 0
    copy = favort.copy()