def squareroot():
    epsilon = 1.e-4
    x = int(input("Enter a positive integer: "))
    while(x<0):
        print("You must enter a positive integer")
        x = int(input("Enter a positive number: "))
#e=estimate, x=target number
    e = x
    while abs(x/e-e) > epsilon:
        e = (x / e + e) / 2
    return e
#using the above defined function
number = squareroot()
print("Square root of the number is", number)

