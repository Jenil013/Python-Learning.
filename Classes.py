#We are creating a new class as Restaurant and we will as few methods to it which gives us the ability to describe the restaurant.

class Restaurant:
  def __init__(self, name, cuisine_type):  #__init__ is a constructor funtion. It is also neccesory to add self as we referring to given calss.
    self.name = name
    self.cuisine_type = cuisine_type

  #Now we will create a method to describe the restaurant.

  def describe_restaurant(self):
    print(f"The name of the restaurant is " + self.name.title() + ".")
    print("The cuisine type of the restaurant is " + self.cuisine_type.title() + ".")


Restaurant1 = Restaurant("KFC", "Fast Food")  #Now we can use Resatuarant as a funtion.
Restaurant1.describe_restaurant()