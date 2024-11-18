import math


class Figure:
    sides_count = 0


    def __init__(self, __color, *sides):
        self.filled = False
        if len(sides) == self.sides_count:
            self.__sides = sides
        else:
            self.__sides = [1] * self.sides_count
        self.__color = __color

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *args):
        for i in args:
            if i > 0 and len(args) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *sides):
        super().__init__(__color, *sides)
        self.__radius = sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * pow(self.__radius, 2)



class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *sides):
        super().__init__(__color, *sides)

    def get_square(self):
        p = self.__len__() / 2
        a, b, c = self.get_sides()
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *sides):
        super().__init__(__color, *sides)
        self.set_sides(*([sides[0]] * self.sides_count))

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)
    cube1 = Cube((222, 35, 130), 6, 8, 9)

    circle1.set_color(55, 66, 77)
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)
    print(cube1.get_color())

    cube1.set_sides(5, 3, 12, 4, 5)
    print(cube1.get_sides())
    circle1.set_sides(15)
    print(circle1.get_sides())

    print(len(circle1))

    print(cube1.get_volume())


    triangle1 = Triangle((121, 213, 163), 2, 3, 2)

    triangle1.set_color(1, 2, 3)
    print(triangle1.get_color())

    triangle1.set_sides(6, 6, 6, 8)
    print(triangle1.get_sides())
    print(triangle1.get_square())
    print(len(triangle1))
