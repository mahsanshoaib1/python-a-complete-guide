#                                   Dictionaries in python

# creating a dictionary
dic1 = {
    "Ahsan": "A programmer",
    "Class": 5,
    "field": "Bioinformatics"
}
# printing the dictionary
print(dic1)
print("\n")

# to access keys in dictionary
print(f"The keys in dic1 are: {dic1.keys()}")
print("\n,")

# to access values in dictionary
print(f"The values in dic1 are:{dic1.values()}")
print("\n")

# explicitly printing
for k in dic1:
    print(k)
print("\n")

# explicitly printing
for k in dic1:
    print(dic1[k])
    
print(dic1.items())
print("\n")

for k,v in dic1.items():
    print(k,v)
   
                            # methods in dictionary

dic1 = {
    "Ahsan": "A programmer",
    "Class": 5,
    "field": "Bioinformatics"
}
dic2 = {
    "Ali": "A hacker",
    "class": 4,
    "Field": "Bioinformatics"
}

# to update a dictionary
dic1.update(dic2)
print(f"The updated dictionary is: {dic1}")

# to empty it
dic1.clear()
print(dic1)

# to remove a value
dic2.pop("class")
print(dic2)

# to remove last value
dic2.popitem()
print(dic2)

# to del whole dictionary
del dic1

# to del a value
del dic2["Ali"]
