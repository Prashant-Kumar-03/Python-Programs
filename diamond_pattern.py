n=int(input("enter a number: "))
for i in range(n//2):
    print(" "*((n//2)-i)+'* '*(i+1))

for i in range(1,(n//2)):
    print(" "*(i+1)+'* '*((n//2)-i))
     
