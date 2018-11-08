def add(a, b):
    return a + b

def safe_add(a, b):
    if type(a) != type(b):
        print("타입이 안맞아서 계산 안됩니다.")
        return
    else:
        result = add(a,b)
    return result

# 아래 if문 안쓰면 mod1.py를 다른 py에서 import하고 실행했을 때 mod1.py도 같이 실행되는 문제 발생!
if __name__ == "__main__":
    print("mod1", __name__)
    print(add(10, 20))
    print(safe_add(1,4))
    print(safe_add(10, 10.4))
    print(add('b', 2)) # error
