
class HouseKim:
    lastname = "김"
    fullname = ""
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("{}, {} 여행을 가다! ".format(self.fullname, where))
        