#  check if an employee has achieved his weekly target or not


class Employee:

    name = "Ben"  # This Class Attribute
    designation = "Sales Executive"
    salesMadeThisWeek = 6

    def hasAchivedTraget(self):
        if self.salesMadeThisWeek >= 5:
            print(" Target Has Been Achived! ")
        else:
            print("Target Has Not Been Achived! ")


employeOne = Employee()

print(employeOne.name)

print(employeOne.hasAchivedTraget())

employeeTwo = Employee()

print(employeeTwo.name)
