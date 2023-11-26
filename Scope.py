#Scope : what variable do i have access to?

# there are two types of scope(access of variable): Global scope and loal scope.

#If any variable is created outside any func than it is called global scope.

def func():
   x = 5
   print(x)

func()
print(x)

 # if we try to print x outside the func it will throw an error.


#Order or Priority of Scope
# Local Scope > Parent function Scope > Global Scope > Built in Scope.

#To use global variable we have to import it using global.



Total = 10

def count(): 
  global Total   #Here I use global to access Total.
  Total += 5
  return print(Total)


#Use nonlocal keyword to use one stage upper scope.




