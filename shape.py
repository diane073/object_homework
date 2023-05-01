class Shape():
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return (self.radius ** 2) * 3.14

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length
    
circle = Circle(5)
rectangle = Rectangle(5, 10)

print(circle.get_area())
print(rectangle.get_area())


