# Multilevel Inheritance

class MusicalInstruments:
    numberOfMajorKeys = 12


class StringInstruments(MusicalInstruments):
    typewood = "Tonewood"


class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print("This Guitar consists of {} strings. It is made of {} and it can play {} keys".format(self.numberOfStrings, self.typewood,self.numberOfMajorKeys))


guitar = Guitar()


