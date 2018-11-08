# file6.py
dic = {}
f = open('README.txt', 'r')
for line in f: # 1줄씩 읽음
    line = line.replace('\n', '') # 줄바꿈 기호 삭제!
    words = line.split() # default : " "
    for word in words:
        if word in dic:
            dic[word] += 1 # 'line' : 3
        else:
            dic[word] = 1 # 'First' : 1

f.close()

for word in dic:
    print(word, dic[word])
    
"""
First 1
line. 3
Second 1
Third 1
"""