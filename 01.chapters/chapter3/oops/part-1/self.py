class Employee:

  def employeeDetails(self):
      # pass
      self.name = "Mathew"
      print("Name is:" self.name)
      
      age = 30 # Attribute without self Obj
      print("Age is:", age)
      
  def printEmployee(self):
      print("printing in another method")
      print("Name: ", self.name ) # we can access the name attribute from above employeeDetails method but not the age 
      print("Age: ", age) # this will get error 
  
      
employee = Employee()

employee.employeeDetails()

employee.printEmployee()

# Employee.employeeDetails(employee) # In This way the python interpreter is taking the code, So the Self is Reffering to an Object i.e,, employee .



