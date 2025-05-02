class Restaurant:
    name = ""
    category = ""
    rating = 0.0
    delivery = False
    
bobsBurgers = Restaurant()
bobsBurgers.name = "Bob\'s Burgers"
bobsBurgers.category = "American Diner"
bobsBurgers.rating = 4.7
bobsBurgers.delivery = False

print(vars(bobsBurgers))