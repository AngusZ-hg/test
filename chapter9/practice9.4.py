class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        pass

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())
    
    def open_restaurant(self):
        print(self.restaurant_name + ' is opening!')
    
    def set_number_served(self):
        self.number_served += 1
    

my_restaurant = Restaurant('lanao', 'Chinese')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print(my_restaurant.number_served)
my_restaurant.number_served = 10
print(my_restaurant.number_served)
my_restaurant.set_number_served()
print(my_restaurant.number_served)