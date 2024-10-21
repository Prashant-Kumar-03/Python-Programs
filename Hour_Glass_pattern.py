n = int(input("Enter a number: "))
x = n // 2
for i in range(x):
    print(" " * i + '* ' * (x - i))
for i in range(2,x+1):
    print(" " * (x - i) + '* ' * (i))
