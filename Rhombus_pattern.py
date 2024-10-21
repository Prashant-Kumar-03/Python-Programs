n = int(input("Enter how many *'s you need: "))
p = int(input("enter how many line you want"))
for i in range(p):
    spaces=" "*i
    print(spaces+'* '*(n))

