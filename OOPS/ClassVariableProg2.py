class Indian():
    default_language='Hindi'
    religion='Hindu'

    def __init__(self,capital,state_rank,food='Biriyani'):
        self.capital=capital
        self.state_rank=state_rank
        self.food=food

    def state_details(self):
        print "Language:{0}".format(self.default_language)
        print "Capital:{0}".format(self.capital)
        print "State_rank:",(self.state_rank)
        print "Religion:",(self.religion)

        print ("***************")


person1=Indian('Bhubaneswar',1,'Dahiwada')
person1.default_language='oriya'
person1.state_details()

person2=Indian('Hyderabadr',2)
person2.religion='Mushlim'
person2.state_details()


