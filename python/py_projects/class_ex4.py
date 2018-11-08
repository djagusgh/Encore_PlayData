# class_ex4.py

from class_ex3 import HouseKim

kim = HouseKim("기사")
kim.travel("태국")

class HouseGo(HouseKim):
    lastname = "고"

go = HouseGo("길동")
go.travel("깐따삐아")

class HouseMa(HouseKim):
    lastname = "마"
    # method overriding
    def travel(self, where, day):
        print("{}, {} 여행 {}일 간다!".format(self.fullname, where, day))

ma = HouseMa("이콜")
ma.travel("파리", 30)