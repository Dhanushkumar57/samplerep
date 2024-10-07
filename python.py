n=int(input("Enter the number:"))
if(n < 0 or n == 0):
    print("The value must be greater than zero")
else:
    fact = 1
    while(n != 0):
        fact = fact * n
        n -=1
    print(fact)