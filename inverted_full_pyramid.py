n = int(input("Enter any number: "))
for i in range(n):
    spaces=" "*i
    print(spaces+'* '*(n-i))