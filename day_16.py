                                # finally keyword
# try:
#     l =  [3,5,1,8,6,9]
#     i = int(input("wite a number: "))
#     print("the value at index is: ", l[i])
# except:
#     print("out of index")
    
# finally:
#     print("The program is successfully executed.")
    
    
def func1(i):
    try:
        l =  [3,5,1,8,6,9]
        i = int(input("wite a number: "))
        print("the value at index is: ", l[i])
        return 0
    except:
        print("out of index")
        return 1
    finally:
        print("The program is successfully executed.")
        
    # print("The program is successfully executed.") # will not be excecuted
x = func1()
print(x)

# in function, if we write print without finally, it will not be excecuted. 