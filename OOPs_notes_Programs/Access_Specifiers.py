# Access Specifiers

# Public - member name :: Accessible anywhere in the program
# Protected - _member name :: Accessible only to the Base class and Derived class
# Private - __member name  :: Accessible only inside the class

class Car:
    numberOfWheels = 4
    _color = "Black" # Protected Attribute
    __yearofManufacture = 2017 # Private Attribute

class Bmw(Car):
    def __init__(self):
        print("Protected attribute color:",self._color)


car = Car()
print("Public attribute:", car.numberOfWheels)
bmw = Bmw()
print("Private attribute :", car._Car__yearofManufacture)   # ___yearofManufacture is internal stored as _Car__YearofManufacture



