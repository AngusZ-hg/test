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

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'strawberry', 'apple', 'lemon']
    
    def show_flavors(self):
        print("We have ice cream with these flavors: ")
        for flavor in self.flavors:
            print(flavor, end=' ')
        print("\nPlease select one you prefer.")

my_icecream = IceCreamStand('lanao', 'icecream stand')
my_icecream.show_flavors()
