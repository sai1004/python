# About Class
class Employee:

    numberOfWorkingHours = 40  # class attribute


employeeOne = Employee()

print("EmpOne :", employeeOne.numberOfWorkingHours)

# o/p: EmpOne : 40

employeeTwo = Employee()

print("EmpTwo :", employeeTwo.numberOfWorkingHours)

# o/p: EmpTwo : 40

# What if you want to change the class attribute value, for that need to access it by class

Employee.numberOfWorkingHours = 45

print("EmpOne :", employeeOne.numberOfWorkingHours)

# o/p: EmpOne : 45


""" Instance Attribute """

employeeOne.name = "John"

print(employeeOne.name)

employeeTwo.name = "mary"

print(employeeTwo.name)

# Chaning The Value Of the empOne WorkingHours

employeeOne.numberOfWorkingHours = 40

print(employeeOne.numberOfWorkingHours)

# empOne Value is not effected to the empTwo

print(employeeTwo.numberOfWorkingHours)
