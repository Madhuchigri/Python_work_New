# overloading an operator
# Example
class Square:
    def __init__(self,side):
        self.side = side

    def __add__(squareOne, squareTwo): # Overloading existing add method
        return (4*squareOne.side) + (4*squareTwo.side)


squareOne = Square(10)
squareTwo = Square(20)
print("Sum of the sides of 2 squares:", squareOne+squareTwo)

# Operator Overloading Excercise
"""Create a class called Square and perform the following tasks -
(i) Create two objects for this class squareOne and
squareTwo
(ii) Find the result of side of squareOne to the power of side
of squareTwo
Example: If squareOne has length of 2cm each side and
squareTwo has a length of 4cm each side, squareOne **
squareTwo should return 16, which is 2 to the power of 4."""


class Square_pow:
    def __init__(self,side):
        self.side = side

    def __pow__(squareOne_pow, squareTwo_pow):
      return (squareOne_pow.side **squareTwo_pow.side)


squareOne_pow = Square_pow(2)
squareTwo_pow = Square_pow(4)

print("square one to the power of side square two is:", squareOne_pow**squareTwo_pow)
