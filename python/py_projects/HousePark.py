class HousePark:

    lastname = "박"

    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("{} {} 여행을 간다!".format(self.fullname, where))
    def __del__(self):
        print("{} 죽네!".format(self.fullname))