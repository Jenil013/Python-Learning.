# Sets are unordered collection of unique elements.
#what make sets different from list is that it only print or store unique values.
 
my_sets = {'jenil', 'patel', 'jenil', 'patel', 'patel', 'patel'}          
 print (my_tuple)

# To make sets use {}.

#Sets Methods:

# To add elements to a set use add() method.
# To clear a set use clear() method.
# To copy a set use copy() method.
# To get the difference between two sets use difference() method.
# To get the difference between two sets and update the first set use difference_update() method.
# To get the intersection between two sets use intersection() method.
# TO pop type .pop(), it will pop the first digit.

set1 = {1,2,3,4,5,6,7,7,7,8,8}
my_set2 = {5,6,7,7,7,8,8,9,10,11,12}

print(my_set1.difference(my_set2)) 
my_set2.discard(8) # To remove
print(my_set2)
print(my_set1.intersection(my_set2))
print(my_set1.isdisjoint(my_set2)) # To check if two sets are anything in comman
print(my_set1.issubset(my_set2)) # To check if set1 is subset of set2
print(my_set1.issuperset(my_set2)) # To check if set1 is superset of set2
print(my_set1.union(my_set2))  # To get the union of two sets or get united  #OR
print(my_set1 | my_set2) 

