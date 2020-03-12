class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+'@compny.com'

    def details(self):
        print "Full Name : {0} {1}".format(self.first,self.last)
        print "Email : {0} ".format(self.email)
        print "Salary :{0}".format(self.pay)

emp1=Employee('Aurobinda','Nayak',5000)
emp2=Employee('Raj','Obreo',7000)

emp1.details()
print '**********************************'
Employee.details(emp2)


