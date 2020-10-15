# Single level Inheritance

class Apple:
    manufacturer = "Apple.inc"
    contactWebsite = "WWW.apple.com/contacts"

    def contactDetails(self):
        print("To contact us,log on to :", self.contactWebsite)


class MacBook(Apple):
    def __init__(self):
        self.yearofManufacture = 2017

    def manufacturerDetails(self):
        print("This MACbook is manufactured in the year {} by {}".format(self.manufacturer, self.yearofManufacture))


macbook = MacBook()
macbook.manufacturerDetails()
macbook.contactDetails()
