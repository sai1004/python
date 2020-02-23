class Employee:

    def __init__(self, name, id):  # Creating Constructor

        self.id = id
        self.name = name

    def display(self):

        print(" ID: %d \n Name: %s" % (self.id, self.name))


employee1 = Employee("John", 101)

employee2 = Employee("David", 102)


print(employee1.display())

print(employee2.display())
