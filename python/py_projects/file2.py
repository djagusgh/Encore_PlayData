# file2.py -> 파일 크기 클 때 한 줄씩 읽어서 처리!
try:
    f = open('README.txt' , 'r')
    while True:
        line = f.readline()
        line = line.replace('\r\n', '') # 줄바꿈 안되게 하기!
        if not line:
            break
        print(line)
    f.close()
except Exception as e:
    print(e)
finally:
    if f:
        f.close()