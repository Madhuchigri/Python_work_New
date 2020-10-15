"""Similar to a library management system, write a program to
provide layers of abstraction for a car rental system.
Your program should perform the following:
1. Hatchback, Sedan, SUV should be type of cars that are
being provided for rent
2. Cost per day:
Hatchback - $30
Sedan - $50
SUV - $100
3. Give a prompt to the customer asking him the type of car
and the number of days he would like to borrow and provide the
fare details to the user """

class Car:

    def __init__(self):
        self.carfare = {'Hatchback':30,'Sedan':50,'SUV':100}

    def display_car_fare_details(self):
        print("car Fare per day:")
        print("Hatchback: $", self.carfare['Hatchback'])
        print("Sedan: $", self.carfare['Sedan'])
        print("SUV: $", self.carfare['SUV'])

    def car_fare_calculate(self, cartype,number_days):

        return  self.carfare[cartype]*number_days



car = Car()

while 1:
    print()
    # Menu starts Here
    print("Enter 1 to Display the cars available for Renting")
    print("Enter 2 to book a car")
    print("Enter 3 to Exit")

    userchoice = int(input())

    if userchoice == 1:
        car.display_car_fare_details()
    elif userchoice == 2:
        print("Enter the car type which you would like to rent")
        cartype = input()
        print("Enter Number of Days required for renting")
        number_days = int(input())
        carfare = car.car_fare_calculate(cartype, number_days)
        print("Payable amount is: $", carfare)
    elif userchoice == 3:
        print("Thanks for visiting..!!!")
        quit()
