numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (numbers)
print (numbers[0])
print (numbers[-1])
print (numbers[-2])


# List Methods
# .append()
# .insert()
# .pop()
# .remove()
# .reverse()
# .sort()
# .clear()
# .copy()
# .count()
# .index()
# .extend()
# .copy()
# .remove()
# .pop()
# .clear()
# .pop()
# .clear()
# .pop()

basket = [1, 2, 3, 4, 5]
basket.append(6) # add at the end.
basket.insert(0, 0) # .insert (index, object)
basket.pop(1) #remove the object.
basket.remove(1) #remove the specific object.

basket = ['a', 'b', 'c', 'd', 'e', 'd', 'c']
print (basket.index('c', 0, 4)) # .index (object, start, end)
print ('a' in basket) # true or false keyword
print (basket.count('c')) 
basket.sort() # sort the list or 
print(sorted(basket)) # make a sorted copy and print it without modify.
basket.reverse() # reverse the list.
basket.clear() # clear the list.



print(list(range(50, 100)))  # To print a list from (start, finish)

# To convert list into a string:
basket = ' '.join(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print (basket)

#List Unpacking
a, b, c, *other, d  = [1,2,3,4,5 ,6, 7, 8]
print(b)
print (other)




