item_list={"brain1": [], "brain2": [], "brain3": [], "brain4": []}
fixed_list=["brain1", "brain2", "brain3", "brain4"]
method =""

while method != "quit":
    for x in range(4):
        try:
            print(fixed_list[x],item_list[fixed_list])
            print(x)
            #print(item_list[fixed_list[x]])
        except:
            item_list[fixed_list[x]] = []


    method = input(":")

    if method == "1":
        name = input("Enter Name: ")
        print(name)
        names = []
        names.append(name)
        print(names)
        item = input("Item: ")
        if name == item_list[item]:
            print("You already have the item")
        elif len(item_list[item]) > 0:
            print("somebody already owns this")
        else:
            item_list[item].append(name)
            print(item_list)

    elif method == "2":
        item = input("Item: ")
        remove= item_list.pop(item)
        print(item_list)



print(item_list)

