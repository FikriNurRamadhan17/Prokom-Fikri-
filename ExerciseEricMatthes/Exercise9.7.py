# Exercise 9-7
class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, {self.age} tahun, {self.city}")


class Admin(User):
    """Admin adalah jenis khusus dari User."""

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Hak akses admin:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin("Rina", "Wijaya", 25, "Jakarta")
admin.describe_user()      # warisan dari User
admin.show_privileges()