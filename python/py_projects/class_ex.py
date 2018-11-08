# class_ex.py

class Calc:
    def sum(self, a, b):
        result = a + b
        print("%s + %s = %s" % (a, b, result))

    def sub(self, a, b):
        result = a - b
        print("%s - %s = %s" % (a, b, result))
    
    def multi(self, a, b):
        result = a * b
        print("%s * %s = %s" % (a, b, result))
    
    def divi(self, a, b):
        if b != 0:
            result = a / b
            print("%s / %s = %s" % (a, b, result))
        else:
            print("b에는 0이 오면 안됩니다.")
    
