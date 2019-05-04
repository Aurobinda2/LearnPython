def toUpper(func):
    def inner():
       y=func()
       result=y.upper()
       return result
    return inner

def changeName(func):
    def inner():
        y=func()
        result='Hello Priyambada'
        return result
    return inner

@toUpper
@changeName
def wish():
    return 'Hello Aurobinda'

print(wish())








