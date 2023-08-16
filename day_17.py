                                # short-hand if else
                                
a= 20
b= 20

# statement if (condition) else statement if (condition) else statement
print("A") if a>b else print("=") if a==b else print("B")

c=10 if (a>b) else 20
print(c)


                                # custom error creation
a = int(input("write any value between 1 to 10: "))

if ((a<1) | (a>10)):
    raise ValueError("Value should be between 1 to 10")
print(a)

# we can create our custom error using classes and OOP  


