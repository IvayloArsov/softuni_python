class Circle:
    def __init__(self, radius: int, pi=3.14):
        self.radius = radius
        self.pi = pi

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        area = self.pi * (self.radius ** 2)
        return area

    def get_circumference(self):
        circumference = self.pi * 2 * self.radius
        return circumference


circle = Circle(11)
# circle.set_radius(160)
print(circle.get_area())
print(circle.get_circumference())
print(circle.pi)
