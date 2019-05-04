import datetime

def outerFunc(date):
    def inner():
        print("Hello Today is : {0}".format(date))
    return inner
date=datetime.datetime.now().date()

calltoOuter=outerFunc(date)
calltoOuter()
