# Exercise 9-4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} menyajikan masakan {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")

    def set_number_served(self, jumlah):
        self.number_served = jumlah

    def increment_number_served(self, tambahan):
        self.number_served += tambahan


restaurant = Restaurant("Warung Sari", "Jawa")

print(restaurant.number_served)      

restaurant.number_served = 25           
print(restaurant.number_served)         

restaurant.set_number_served(40)        
print(restaurant.number_served)         

restaurant.increment_number_served(15)  
print(restaurant.number_served)         