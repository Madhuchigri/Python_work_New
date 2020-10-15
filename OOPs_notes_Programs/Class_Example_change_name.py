#  Change the name you previously defined within a method and call this method by making use of the object you created

class Employee:
    employeeName = "Ben"

    def change_name(self):

        Employee.employeeName = "john"


employeeOne = Employee()
print("name before change is :", employeeOne.employeeName)
employeeOne.change_name()
print("name after change is :", employeeOne.employeeName)

