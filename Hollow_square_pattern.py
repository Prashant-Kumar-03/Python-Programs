n=int(input("enter any number: "))
for i in range(n):
    if(i==0 or i==n-1):
        print("* "*n)
    else:
        print("*"+" "*((n-1)*2-1)+"*")