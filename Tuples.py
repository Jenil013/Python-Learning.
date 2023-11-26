# Tuple are list which cannot be modified.

#tuple has only two methods:
# (1) Count() : Counts the number of times a specified value occurs in a tuple.
# (2) index() : Returns the index of the first occurrence of a specified value.

my_tuple = ('jenil', 'patel', 'jenil', 'patel', 'patel', 'patel')
print (my_tuple.count('jenil'))
print (my_tuple.index('patel'))