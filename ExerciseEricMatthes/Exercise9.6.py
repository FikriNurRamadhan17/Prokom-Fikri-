# Exercise 9-6
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} menyajikan masakan {self.cuisine_type}.")


class IceCreamStand(Restaurant):
    """Kedai es krim, turunan dari Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanila", "coklat", "stroberi"]

    def show_flavors(self):
        print(f"Rasa yang tersedia di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


stand = IceCreamStand("Es Krim Ceria", "Es Krim")
stand.describe_restaurant()   # method warisan dari Restaurant
stand.show_flavors()