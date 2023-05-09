class Mobile:
    def __init__(self,name):
        self.name = name 


class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobile.appemd(new_mobile)
        else:
            raise TypeError('new mobile should be object of Mobile Class')

oneplus = Mobile('one plus 6 ')
samsung = 'samsung galaxy s8'
mobostore = MobileStore() 
print(mobostore.mobiles)
mobostore = MobileStore() 