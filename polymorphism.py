class Hewan:
    def __init__(self, name):
        self.name = name

    def suara(self):
        return "hewan bersuara"

class Sapi(Hewan):
    def suara(self):
        return "MOO"

class Kambing(Hewan):
    def suara(self):
        return "mbekk"

hewan_list = [  #polymorphism in action
    Sapi("dessy"),
    Kambing("kacung")
]

for hewan in hewan_list: #method sama, behavior berbeda
    print(hewan.suara())

#duck typing
class Mobil:
    def start(self):
        print("Mobil berjalan")


class Motor:
    def start(self):
        print("Motor berjalan")


class Perahu:
    def start(self):
        print("Perahu berjalan")


def operasikan_kendaraan(kendaraan): #funct yg polymorphic
    kendaraan.start()

# polymorphism dgn duck typing
kendaraan_list = [
    Mobil(),
    Motor(),
    Perahu()
]

for kendaraan in kendaraan_list:
    operasikan_kendaraan(kendaraan)


# abstract method
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shape_list = [
    Rectangle(10, 20),
    Circle(10)
]

for shape in shape_list:
    print(shape.area())