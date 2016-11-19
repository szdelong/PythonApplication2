class worker:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay*=(1.0+percent)

bob=worker('Bob Smith',5000)
print bob