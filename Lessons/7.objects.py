"""
🐍 This Python file serves as a demonstration of objects in Python.
It includes examples and explanations of how to create and manipulate objects using classes.
"""

# Objects

# 🧱 Example 1: Creating a class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

# 🚗 Example 2: Creating objects from a class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)

# 🖨️ Example 3: Accessing object attributes and methods
car1.display_info()
car2.display_info()

# 🛠️ Example 4: Modifying object attributes
car1.year = 2022
car1.display_info()

# 💥 Example 5: Deleting object attributes
del car2.year
# print(car2.year)  # This will raise an AttributeError

# 🧩 Example 6: Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model} (Electric)")

# ⚡ Example 7: Creating objects from a subclass
electric_car = ElectricCar("Tesla", "Model S", 2021, "100 kWh")
electric_car.display_info()

# Tasks:
# 😎 Create a class representing a person with attributes name, age, and gender.
# 📏 Create objects for three different people and display their information.
# 🤔 Create a class representing a rectangle with attributes length and width, and a method to calculate its area.
# 😄 Create an object representing your favorite book with attributes title, author, and year of publication.
# 🌈 Create a class representing your smartphone with attributes brand, model, and price.
# 🎲 Create a class representing your future bank account with attributes account number, balance, and owner's name.
# 🎇 Add deposit and withdraw methods to your future bank account class
