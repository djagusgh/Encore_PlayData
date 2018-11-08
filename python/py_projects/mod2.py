# mod2.py

PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)

def add(a, b):
    return a + b

if __name__ == '__main__':
    print(PI) # 3.141592
    a = Math() # 객체 생성, 자바의 new 키워드를 안 붙임
    print(a.solv(2)) # 12.566368, 객체.메소드로 실행
    print(add(PI, 4.4)) # 