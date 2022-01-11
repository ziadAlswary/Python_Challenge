names= list()
i=1
opt = "yes"
print("Enter names of three people you want to invite them to the party:")
while opt != "no":
    name = input("   Name {0}: ".format(i))
    names.append(name)
    i+=1
    if i > 3:
        opt = input("Do you want to add another (yes|no)? ")

print("\nnumber of people you have invited to the party is : ",len(names))
        
        