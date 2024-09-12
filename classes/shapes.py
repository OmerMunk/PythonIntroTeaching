class Shape:
    def __init__(self, nodes, color):
        self.nodes = nodes
        self.color = color

    def print_color(self):
        print(f'color: {self.color}')

class Puki:
    pass


class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(0, color)
        self.radius = radius

class Square(Shape):
    def __init__(self, length, color):
        super().__init__(4, color)
        self.length = length

if __name__ == "__main__":
    c1 = Circle(20, "red")
    c2 = Circle(20, "yellow")
    print