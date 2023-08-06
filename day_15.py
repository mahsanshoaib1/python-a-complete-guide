                            # else with for loop and exception handling

for i in range (5):
    print(i)
else:
    print("there is no i")
    
# if we break the loop then else will not work

for i in range (5):
    print(i)
    if i==4:
        break
else:
    print("there is no i")
    
    
# exception handling
# example 1
try:
    a  = int(input("write a number: "))
    for i in range(1,11):

        print(f"{a} x {i} = {a*i}")
except Exception as e:
    print("kyon maa c rha hy")    
    
print("End of program")

# example 2
try:
    a  = int(input("write a number: "))
    for i in range(1,11):

        print(f"{a} x {i} = {a*i}")
except:
    print("kyon maa c rha hy") 
 

# example 2   
try:

    a  = int(input("write a number: "))

    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")

except ValueError:

    print("kyon maa c rha hy") 