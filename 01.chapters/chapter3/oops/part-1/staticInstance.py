# static and instance methods:

class Employee:

    def employeeDetails(self):
        self.name = "Ben" #Attribute
        
    @staticmethod # by implemnting static method, enabling to dont throw error on not passing self parm in method
    def welcomeMessage():
        print("welcome to our Organisation! ")
      
employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()


