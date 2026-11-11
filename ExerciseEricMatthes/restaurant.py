# Exercise 9-10 (restaurant.py)
"""Module berisi class Restaurant."""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} menyajikan masakan {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")