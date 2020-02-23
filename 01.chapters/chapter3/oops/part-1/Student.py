class Student:

    def set_student_id(self, id):
        self.__setStudentId = id  # __setattr__

    def set_eng_pass_of_year(self, year):
        self.__setYearOfPass = year

    def get_student_id(self):

        return self.__setStudentId

    def get_eng_pass_year(self):

        return self.__setYearOfPass


setObj = Student()

setObj.set_student_id(1004)

setObj.set_eng_pass_of_year(2001)

print("Student Id: ", setObj.get_student_id())
print("Engg Pass Of Year: ", setObj.get_eng_pass_year())
