# Codecademy Oriented Object Project - OOP

# Objective:
# The aim of this guided project was apply several concepts regarding to
# OOP and the lessons studied in ML engineer path of Codecademy
# To a Italian Restaurant!

# Note: Each comment specify an special instruction and the class and
# functions created doesn't have the Doc string rules......

# Import packages:
from datetime import time
import pandas as pd


"""
0. At Basta Fazoolin' with my Heart our motto is simple: when you're here with 
family, that's great! We have four different menus: brunch, early-bird, dinner, 
and kids.

1. Create a Menu class
2. Give Menu a constructor with the five parameters self, name, items, 
   start_time, and end_time.
"""

class Menu():
  def __init__(self, name:str, items:dict, start_time:time, end_time:time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
    """ 3. Give our Menu class a string representation method that will tell you the 
        name of the menu. Also, indicate in this representation when the menu is available.
    """

  def __repr__(self):
    msg = "{} menu available from: {}pm to {}pm".format(self.name, self.start_time, self.end_time)
    return msg

  """ 4. Give Menu a method .calculate_bill() that has two parameters: 
      self, and purchased_items, a list of the names of purchased items.

      Have calculate_bill return the total price of a purchase consisting 
      of all the items in purchased_items.
  """  

  def calculate_bill(self, purchased_items: list):
    total_bill = []
    self.purchased_items = purchased_items
    for clave, valor in self.items.items():
      for m in range(len(purchased_items)):
        if purchased_items[m] == clave:
          total_bill.append(valor)
    return "Total bill: {}".format(sum(total_bill))

""" 4. Let's create our first menu: brunch. Brunch is served from 11am to 4pm 
"""

brunch = Menu('brunch', 
    { 'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 
    'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
    },
    time(11, 0) , time(16, 0) 
    )

""" 5. Let's create our second menu item early_bird. Early-bird Dinners 
    are served from 3pm to 6pm. The following items are available 
    during the early-bird menu
"""

early_bird = Menu('early_bird', 
    {'salumeria plate': 8.00, 
     'salad and breadsticks (serves 2, no refills)': 14.00, 
     'pizza with quattro formaggi': 9.00, 
     'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 
     'coffee': 1.50, 'espresso': 3.00,
    },
    time(15, 0, 0) , time(18, 0, 0) 
    )



""" 6. Let's create our third menu, dinner. Dinner is served from 5pm to 11pm.
     The following items are available for dinner:
"""

dinner = Menu('dinner', 
              { 'crostini with eggplant caponata': 13.00, 
                'caesar salad': 16.00, 
                'pizza with quattro formaggi': 11.00, 
                'duck ragu': 19.50, 
                'mushroom ravioli (vegan)': 13.50, 
                'coffee': 2.00, 'espresso': 3.00,
              },
              time(17, 0, 0) , time(23, 0, 0) 
              )

""" 7. And let's create our last menu, kids. The kids menu is available from 
    11am until 9pm. The following items are available on the kids menu.
"""

kids = Menu('kids', 
            {'chicken nuggets': 6.50, 
            'fusilli with wild mushrooms': 12.00, 
            'apple juice': 3.00
            },
            time(11, 0, 0) , 
            time(21, 0, 0) 
            )

""" 8. Try out our string representation. If you call print(brunch) 
    it should print out something like the following: 
    brunch menu available from 11am to 4pm
"""
print(brunch)

""" 9. Test out Menu.calculate_bill(). We have a breakfast order for 
    one order of pancakes, one order of home fries, and one coffee. 
    Pass that into brunch.calculate_bill() and print out the price.
"""

print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))

""" 10. What about an early-bird purchase? Our last guests ordered the 
    salumeria plate and the vegan mushroom ravioli. Calculate the 
    bill with .calculate_bill().
"""
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

""" 11. Basta Fazoolin' with my Heart has seen tremendous success with the family 
    market, which is fantastic because when you're at Basta Fazoolin'
    with my Heart with family, that's great!
    
    We've decided to create more than one restaurant to offer our fantastic menus,
     services, and ambience around the country.

    First, let's create a Franchise class.
"""

class Franchise:

  """ 12. Give the Franchise class a constructor. Take in an address, and assign
   it to self.address. Also take in a list of menus and assign it to self.menus.
  """
  def __init__(self, address: str, menus: list):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address  

  def available_menus(self, time: time):
    self.time = time
    #available_menus = []
    for k in range(len(self.menus)):
      if self.menus[k].start_time <= self.time and self.time <= self.menus[k].end_time:
        df_dict = pd.DataFrame.from_dict(self.menus[k].items, orient='index', columns=['Product and price'])
        print("Available menu {}: {}".format(self.menus[k].name, df_dict))

 

""" 13. Let’s create our first two franchises! Our flagship store is located at 
    "1232 West End Road" and our new installment is located at 
    "12 East Mulberry Street". Pass in all four menus along with these 
    addresses to define flagship_store and new_installment.
"""

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])


""" 14. Give our Franchises a string representation so that we'll be able to tell 
    them apart. If we print out a Franchise it should tell us the address of 
    the restaurant.
"""
print(flagship_store)
print(new_installment)

""" 15. Let's tell our customers what they can order! Give Franchise an .available_menus()
    method that takes in a time parameter and returns a list of the Menu objects 
    that are available at that time.
    
    Let's test out our .available_menus() method! Call it with 12 noon as an argument
    and print out the results.
"""

print(flagship_store.available_menus(time(12,0)))

""" 16. Let’s do another test! See what is printed if we call .available_menus() 
    with 5pm as an argument and print out the results.
"""
print(new_installment.available_menus(time(17,0)))

""" 17. Since we've been so successful building out a branded chain of restaurants, 
    we've decided to diversify. We're going to create a restaurant that sells arepas!

First let's define a Business class.

Give Business a constructor. A Business needs a name and a list of franchises.
"""

class Business:
  
  def __init__(self, name: str, franchises: list):
    self.name = name
    self.franchises = franchises

""" 18. Before we create our new business, we’ll need a Franchise and before 
    our Franchise we’ll need a menu. The items for our Take a’ Arepa 
    available from 10am until 8pm are the following:
"""

arepas_menu = Menu("Take a’ Arepa", 
                  {'arepa pabellon': 7.00, 
                   'pernil arepa': 8.50, 
                   'guayanes arepa': 8.00, 
                   'jamon arepa': 7.50}, 
                   time(10,0), time(20,0))



""" 19. Let's create our first Business. The name is "Basta Fazoolin' with my Heart" 
    and the two franchises are flagship_store and new_installment.

"""
Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

""" 20. Next let's create our first Take a' Arepa franchise! Our new restaurant is 
    located at "189 Fitzgerald Avenue". Save the Franchise object to a variable 
    called arepas_place.
"""

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

""" 21. Now let's make our new Business! The business is called "Take a' Arepa"!§
"""

Business("Take a' Arepa", [arepas_place])


""" 22. Congrats! You created a system of classes that help structure your code 
    and perform all business requirements you need. Whenever we need a new 
    feature we’ll have the well-organized code required to make developing 
    and shipping it easy.
"""











