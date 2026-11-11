# Exercise 9-2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} menyajikan masakan {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")


restaurant_1 = Restaurant("Warung Sari", "Jawa")
restaurant_2 = Restaurant("Sushi Tei", "Jepang")
restaurant_3 = Restaurant("Pizza Hut", "Italia")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

