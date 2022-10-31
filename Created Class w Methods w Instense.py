class student:
    # class properites
    stuCount = 0
    
    #class methods
    def _init_(self, stuIdNum, lastname, firstname):
        self.stuIdNum = stuIdNum
        self.lname = lastname
        self.fname = firstname
        
    def displayStudent(self): 
        print('Student Id :', self.stuIdNum,', Last Name : ', self.lname,', First Name: ', self.fname)
        
    def displayStuCount(self):
        print("Total Students %d" % Student.stuCount)
        
student1 = Student(1000, 'Cohen', 'Bob')
print(type(student1))
student.displayStudent()
student.displayStuCount()

