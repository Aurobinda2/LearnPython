class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+'@compny.com'



emp1=Employee('Aurobinda','Nayak',5000)
emp2=Employee('Raj','Obreo',7000)

# emp1.first='Aurobinda'
# emp1.last='Nayak'
# emp1.email=emp1.first+emp1.last+'@compny.com'
#
# emp2.first='Andrew'
# emp2.last='Dash'
# emp2.email=emp1.first+emp1.last+'@compny.com'

print emp1.email
print emp2.first
print emp1.first

