# file8.py
f = open('new.txt', 'a')
for i in range(11, 21):
    data = "{} line!\n".format(i)
    f.write(data)
f.close()