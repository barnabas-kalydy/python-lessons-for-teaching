# Example 1: Creating a simple class
class Person:
    # This is the constructor of the class:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Example 2: Creating an object of the class
person1 = Person("Alice", 25)

# Example 3: Accessing object attributes
print("Name:", person1.name)
print("Age:", person1.age)

# Example 4: Modifying object attributes
person1.age = 30
print("Modified age:", person1.age)

# Example 5: Adding methods to a class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Example 6: Creating an object and calling a method
circle1 = Circle(5)
print("Area of the circle:", circle1.area())

# Example 7: Inheritance
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

# Example 8: Creating an object of the subclass
student1 = Student("Bob", 20, "Computer Science")
print("Student's major:", student1.major)

# Exercises
# Exercise 1: Create a class representing a book with attributes title, author, and pages.
# Exercise 2: Create an object of the class and print its attributes.
# Exercise 3: Modify one of the attributes of the object.
# Exercise 4: Add a method to the class to get the number of pages.
# Exercise 5: Create a subclass of the book class representing an e-book with an additional attribute format.
# Exercise 6: Create an object of the e-book class and print its attributes.
# Exercise 7: Override the method to get the number of pages in the e-book class.
# Exercise 8: Create a method in the e-book class to check if it's compatible with Kindle.
