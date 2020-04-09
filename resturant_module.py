class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type  
    def describe_restaurant(self):
        print("The name of this restaurant is: " + self.restaurant_name.title() + " and they serve: " + self.cuisine_type.title() + ".")
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open.")
    
restaurant = Restaurant('Jacobs', 'Steak')
print("This restaurant name is: " + restaurant.restaurant_name + ".")    
print("They serve: " + restaurant.cuisine_type.title() + ".")

restaurant.describe_restaurant()
restaurant.open_restaurant()