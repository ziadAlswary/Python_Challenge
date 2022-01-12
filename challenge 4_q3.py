n = int(input("how many people you wanto invite to a party ? \n   -> "))

if n < 10:
    for i in range(1,n+1):
        print("Person {i_} name : ".format(i_ = i),end="")
        name = input()
        print("[{0}] has been invited\n".format(name))
else: print("\n\tToo many people :(\n")