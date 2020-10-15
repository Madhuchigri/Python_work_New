# Multiple Inheritance

class OperatingSystem: # Base class
     multitasking = True


class Apple:
    website = "WWW.Apple.com"


class Macbook(OperatingSystem,Apple):
    def __init__(self):
       if  self.multitasking is True:
           print("This is a multitasking System. Visit {} for more Details".format(self.website)


macbook = Macbook()

