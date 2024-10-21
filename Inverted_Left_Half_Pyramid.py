n = int(input("Enter any number: "))
for i in range(n):
    spaces = " " * (2 * i)  
    print(spaces + '* ' * (n - i))
