#Loop creates the itration of the code.


for fruits in ['apple', 'banana', 'orange', 'mango']:
  for numbers in range (1, 5):
    print (fruits, numbers)   # This is called Nesting/


#Iterables = Lists, Tuples, Dictionaries, Set, Strings.

#For Dictionary

users = {'name': 'Jenil'
  ,'age': 50,
  'country': 'India'}
for x in users.values():  # This will iterate the values of the dictionary.
  print (x)
for y in users.items():  # This will iterate the items of the dictionary.
  print (y)

#Sum up Exercise

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0 # Created a counter variable for reference.

for x in my_list:
  counter = counter + x

print(counter)

for char in enumerate('Python'):  #This will be helpful to track the index of iteration.
  print(char)
