def parentFunc():
    print('Hello I am parent function, I am returning a child function..')
    return child

def child():
    print('Hello I am child function return from parent functiion')

x=parentFunc()
x()
