favort = []
exitt = False
num_in_list = 0
numb= 0
while not exitt:
    is_where_inportan = input("do you care where it is in the list? (y/n)")
    if is_where_inportan == "y":
         where= input(int("enter where in the list?(number)"))
         thing_add_to_list = input("what is one of your favorite movie/shows?(say exit to exit)")
         if thing_add_to_list == "exit":
             exitt = True
         else:
            where= where - 1
            favort.insert(where,thing_add_to_list)
            num_in_list = num_in_list + 1
            for i in favort:
                 print(favort[numb])
                 numb = numb + 1
            numb = 0
    elif is_where_inportan == "n":
        thing_add_to_list = input("what is one of your favorite movie/shows?(say exit to exit)")
        if thing_add_to_list == "exit":
            exitt = True
        else:
            favort.append(thing_add_to_list)
            num_in_list = num_in_list + 1
            for i in favort:
                print(favort[numb])
                numb=numb+1
            numb = 0