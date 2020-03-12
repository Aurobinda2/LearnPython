class student():
    department="MCA"
    roll_prefix='MC'
    male_salute='Mr.'
    female_salute='Miss.'
    male_count=0
    female_count=0
    def __init__(self,name,gender,roll_id):
        self.name=name
        self.gender=gender
        self.email=name+"@school.co.in"
        self.roll=student.roll_prefix+roll_id

    @classmethod
    def student_department_modificatio(cls,department,roll_prefix):
        flag=cls.prompt()
        if flag =='y' or flag =='Y':
             cls.department=department
             cls.roll_prefix=roll_prefix
        elif flag=='n' or flag=='N':
           print "Don't worry ! we will keep your details as before. "

    @staticmethod
    def prompt():
        print "Your department and roll_prefix will be change for following students,\
          because you call class method 'modification student',\
          You can change it again by call 'student_department_modificatio' method "
        input1=raw_input("Press Y/N : ")
        return input1


    def student_details(self):
        print "Roll: {}".format(self.roll)
        if self.gender=='Male':
           print "Name : {0} ".format(self.male_salute+''+self.name)
        else:
            print "Name : {0} ".format(self.female_salute+''+self.name)
        print "Gender : {0} " .format(self.gender)
        print 'Deparment : {0}'.format(self.department)
        print  'Email :{0}'.format(self.email)
        print"*********************************"

s1=student('Divya','Female','5324')
s1.student_details()
student.student_department_modificatio('BSC','BS')
s2=student('Arivind','Male','5431')
s2.student_details()









