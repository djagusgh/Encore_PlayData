#test_input1.py
import random

answer = random.randint(1, 100)
num = 1
print(answer)

while(True):
    guess = int(input("숫자를 입력하세요: "))
    if guess > answer:
        print("답은 더 작은 숫자입니다.")
        num += 1
    elif guess < answer:
        print("답은 더 큰 숫자입니다.")
        num += 1
    else:
        print("축하합니다 {}번만에 정답을 맞추셨습니다".format(num) )
        break 
    
