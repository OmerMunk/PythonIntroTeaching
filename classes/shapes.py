from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, nodes, color):
        self.nodes = nodes
        self.color = color

    def print_color(self):
        print(f'color: {self.color}')

    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(4, color)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Rhombus(Shape):
    def __init__(self, length, diagonal1, diagonal2,color):
        super().__init__(4, color)
        self.length = length
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def calculate_area(self):
        return  self.diagonal1 * self.diagonal2 / 2





class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(0, color)
        self.radius = radius

class Square(Rectangle, Rhombus):
    def __init__(self, length, color):
        super().__init__(4, color)
        self.length = length

if __name__ == "__main__":
    c1 = Circle(20, "red")
    c2 = Circle(20, "yellow")
    print