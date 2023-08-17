                                    # Enumurate
# Enumurate is a function that returns a tuple containing a count/index (from start which defaults to 0)
# and the values obtained from iterating over sequence:

    
a = [21,23,24,25,53,56,56,87,9,90,76]

for m in enumerate (a): # tupe containing two numbers will store in m.
    print(m)
    break


 
for i, m in enumerate (a): # tuple khul jay ga, aur donon values i aur m mein chali jaein gi
    if (i == 4):
        print(m)
        break
    

    