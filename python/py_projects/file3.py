# file3.py => 파일 크기 작을 때 한번에 처리
# list 형태에 txt 파일을 담는데 용량 크면 메모리 터져버림
f = open('README,txt' ,'r')
lines = f.readlines()
print(lines)
print(type(lines)) # 자료형 : list

for line in lines:
    line = line.replace('\n', '')
    print(line)

