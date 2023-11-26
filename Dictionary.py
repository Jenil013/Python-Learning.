#Dictionary: It is an unorderd collection of key-value pairs. It can store any type of data.
dict = {'name': 'jenil', 'age': 20, 'country': 'India'} 
print (dict['age'])

# To add a new key-value pair:
dict['city'] = 'Mumbai'
print (dict)

#We can also create multiple groups in one dictionary:
dict1 = [
  { 'a' : [3,5,8],
  'b' : 2,
  'c' : 'jenil'
},
{'d' : [1,2,3,4],
'e' : [1,2,3,4, 7],
'f' : 'patel'
}
]
print (dict1[0]['b'])   #[group][variable][value]


# DICTIONARY KEY NEED STO BE IMMUTABLE (UNCHANGEABLE) SUCH AS INT, STRING, BOOLEANS ETC.

#if you want to find if any certain key is in the dictionary or not:
print (dict1.get('age'))  #if it is not will get output as None.
print (dict1.get('age', 20))  # To add the key.


# Some Methods
user = { 'a' : [3,5,8],
   'b' : 2,
   'c' : 'jenil'
 }
print ('c' in user.keys()) 
print ('jenil' in user.values())
print(user.pop('a')) # delete the iteam
