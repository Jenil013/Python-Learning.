# Print the repeating objects in a list:

some_list = ['a', 'b', 'c', 'd', 'c', 'e', 'e']

duplicate = []
for value in some_list:
  if some_list.count(value) > 1:
    duplicate.append(value)

print(duplicate)


# Make a pixel tree:

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

for row in Tree:
  for pixel in row:
    if pixel == 1:
      print('*', end='')
    else:
      print(' ', end='')

  print(' ')

#
def age_requirement():
  age = int(input('What is you age: '))
  if age >= 18:
      print('Powering ON, Enjoy ')
  else:
      print('Not old enough')


def highest_evens(li):
  '''
  This function will return the highest even number in a list.
  '''
  evens = []
  for num in li:
    if num % 2 == 0:
      evens.append(num)
  return print(max(evens))

highest_evens([1, 2, 3, 4, 5, 16, 7, 8, 9, 10])