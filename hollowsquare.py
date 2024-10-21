n=int(input())
for i in range(n):
    if(i==0 or i==n-1):
        print("1"*n)
    else:
        print("1"+" "*(n-2)+"1")