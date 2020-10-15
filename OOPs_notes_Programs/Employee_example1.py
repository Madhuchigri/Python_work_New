# check if the Employee has achieved his targets

class Employee: # creating a class
    employeeName = "Ben"
    employeeDesignation = "Sales Executive"
    salesMadeThisWeek = 6

    def has_achieved_target(self): # creating a method
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved")

        else:
            print("Target has not been achieved")


employeeOne = Employee()
print(employeeOne.employeeName)
print(employeeOne.has_achieved_target())
