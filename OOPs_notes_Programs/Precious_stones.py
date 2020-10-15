"""Write an object oriented program to create a precious stone.
Not more than 5 precious stones can be held in possession at a
given point of time. If there are more than 5 precious stones,
delete the first stone and store the new one."""


class Precious_stone:
    numberPrecioustones = 0
    Precious_stone_collection = []

    def __init__(self, name):
        self.name = name
        # increment the number of precious stones
        Precious_stone.numberPrecioustones += 1
        # Append the precious stone to the list if total number of stones are less than 5
        if Precious_stone.numberPrecioustones <= 5:
            Precious_stone.Precious_stone_collection.append(self)

        else:
            del Precious_stone.Precious_stone_collection[0]
            Precious_stone.Precious_stone_collection.append(self)

    @staticmethod
    def displayPreciousstones():
        for precious_stone in Precious_stone.Precious_stone_collection:
            print(precious_stone.name, end = '')
            print()


preciousstoneone = Precious_stone('Ruby')
preciousstoneTwo = Precious_stone('Emerald')
preciousStoneThree = Precious_stone("Sapphire")
preciousStoneFour = Precious_stone("Diamond")
preciousStoneFive = Precious_stone("Amber")
preciousStoneFive.displayPreciousstones()
preciousStoneSix = Precious_stone("Onyx")

# Print all the stones after deleting the first stone
Precious_stone.displayPreciousstones()
