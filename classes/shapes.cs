public class Shape{
    public Shape(int nodes, string color){
         this.nodes = nodes
        this.color = color
    }


    def print_color(self):
        print(f'color: {self.color}')
}





public class Circle : Shape {
    public Circle(radius, color){
       this.radius = radius;
    }
}
    def __init__(self, radius, color):
        super().__init__(0, color)
        self.radius = radius

class Square(Shape):
    def __init__(self, length, color):
        super().__init__(4, color)
        self.length = length

if __name__ == "__main__":
    Circle c1 = new Circle(20, "red")
    c2 = Circle(20, "yellow")
    print