# Exercise 9-3
class User:
    """Profil pengguna sederhana."""

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Kota: {self.city}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang.")


user_1 = User("Fikri", "Ramadhan", 19, "Surakarta")
user_2 = User("Budi", "Santoso", 20, "Semarang")

user_1.describe_user()
user_1.greet_user()
print()
user_2.describe_user()
user_2.greet_user()