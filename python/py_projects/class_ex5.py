
class Fish:
    def __init__(self, name):
        self.name = name
    def swim(self):
        print("수영 가능!")

class Human:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print("걷는다.")

class Mermaid(Fish, Human):
    def __init__(self, name):
        self.name = name

m = Mermaid("인어")
m.walk()
m.swim()
