def greet():
  print ('Hello')

greet()

# Tree Fuction
Tree = [
  [0,0,0,0,1,0,0,0,0],
  [0,0,0,1,1,1,0,0,0],
  [0,0,1,1,1,1,1,0,0],
  [0,1,1,1,1,1,1,1,0],
  [1,1,1,1,1,1,1,1,1],
  [0,0,0,0,1,0,0,0,0,],
  [0,0,0,0,1,0,0,0,0,],
  [0,0,0,0,1,0,0,0,0,]
]
def print_tree():
  for row in Tree:
    for pixel in row:
     if pixel == 1:
        print('*', end='')
     else:
      print(' ', end='')


    print(' ')

print_tree()
print_tree()
print_tree()


#Parameters : If we call a funtion without any given value it will assign a default parameter.

def my_funtion(country = 'India', years = 'born'):  #Example of default parameter
  print (f'I am from {country} since I was {years}')

my_funtion()



#Arguments : Arguments are the values given to the parameters when the function is called. In below code "USA", 'Sweden' are the arguments we assign for paramerters.

my_funtion('USA', 10)
my_funtion ('Sweden')


#RETURN VALUES: TO let funtion return the value use the return.

def cube(num):
  return num*num*num  #Funtion needs to get return in order to execute the code.

print(cube(3))

# To docstring any funtion or explain its use we can simply do:

def cube(num):
  '''
  This funtion will make a cube of a number.
  '''
  num = num*num*num
  print(num)

cube(3)
#TO print the info.:
print(cube.__doc__)


# *args and **kwargs
# *args allows multiple int inputs while **kwargs allows dictionary keys and values inputs.

def func1(*args, **kwargs):
  print(args)
  print(kwargs)
  return print(sum(args) + sum(kwargs.values()))


func1(5,10, num1 = 5, num2 = 15)

#ORDER OF PARAMETERS: 
# 1. Positional Parameters
# 2. *arge
# 3. Default Param.
# 4. **kwargs