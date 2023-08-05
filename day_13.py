#                                    docstrings

def square(n):
    '''Takes an argument as return square of it''' # this is a docstring
    return (n**2)
print(square(5))
print(square.__doc__)

def square(n):
    print(n)
    '''Takes an argument as return square of it''' # now this is not a docstring
    return (n**2)


#                                   Set

s = {2,3,4,5,5} # no duplicate values, unordered, unchangeable
info = {"caral", 10, True, 20, "Hi"}
print(f"The set i created is: {s}")
print(f"The set i created is: {info}")

# empty set
e_set = set()
for v in s:
    print(v)
    
                                # set methods

s1 = {1,2,3,5,4,6,8}
s2 = {2,8,7,4,3,6,1}
# union of both sets (all values in both)
print("the union of both sets is: ", s1.union(s2))
# update set1
s1.update(s2)
print("the updation of both sets is: ", s1)
# intersection (only common)
print("the intersection of both sets is: ", s1.intersection(s2))
# symmetric difference (other than common values)
print("the symmetric difference of both sets is: ", s1.symmetric_difference(s2))
# difference (values present in only 1st set)
print("the difference of both sets is: ", s1.difference(s2))
# disjoint (sets having no common value)
print("the disjoint of both sets is: ", s1.isdisjoint(s2))
# supper set
print("the supperset is: ", s1.issuperset(s2))
# to add a value
s1.add(190)
print("after add functions s1 is: ", s1)
# to remove a value
s1.remove(190) # if value not present through error
s1.discard(90) # if value not present not through error
print("after removal function s1 is: ", s1)
# to remove random a value
r = s1.pop()
print(f"poped value is: {r}")
# to delete the set
del s2
# print(s2) Error
# make set empty set
s1.clear() 
print(s1)
cities = {"pakistan", "germeny", "US", "China"}
if "China" in cities:
    print("china is present")
else:
    print("china is not present")