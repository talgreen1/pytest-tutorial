from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


sqr = Square(4)
rect = Rectangle(2, 3)

print(sqr.area())
print(rect.area())
