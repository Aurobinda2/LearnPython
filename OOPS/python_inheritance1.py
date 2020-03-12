
class A(object):
    def __init__(self, a,x):
        self.x=x
        self.a = a

    def method1(self):
        print "Method1 of class A called "


class B(A):
    def __init__(self, b, a,y):
        A.__init__(self, a)
        self.b = b
        self.y=y

    # method override
    def method1(self):
        print "Method1 of class B called"

# Multilevel inheritance

class C(A,B):
    def __init__(self,x,y,z):
        A.__init__(self,x)
        B.__init__(self,y)
        self.z=z
    A.method1()



a1 = A()
b1 = B(10)
c1=

print dict(A)

print isinstance(a1, A)
print isinstance(a1, B)

print issubclass(B, A)
print issubclass(A, B)











