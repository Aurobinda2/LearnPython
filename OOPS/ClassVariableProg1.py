class Employee:
    raise_amount=1.04
    numberOfEmployee=0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@compny.com'
        Employee.numberOfEmployee+=1

    def details(self):
        print "Full Name : {0} {1}".format(self.first,self.last)
        print "Email : {0} ".format(self.email)
        print "Old_Salary :{0}".format(self.pay)
        print "Raise Amount : {0}".format(Employee.raise_amount)
        print "New Salary {0}".format(self.pay+Employee.raise_amount)
        print "*******************"

    def number_of_employee(self):
        print "Number of employee {0} : ".format(Employee.numberOfEmployee)

emp1=Employee('Aurobinda','Nayak',5000)
emp2=Employee('Raj','Obreo',7000)

emp1.number_of_employee()
#print emp1.number_of_employee()

emp1.details()
Employee.details(emp2)



