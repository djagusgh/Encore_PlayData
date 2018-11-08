#file7.py

f = open('new.txt', 'w')
for i in range(1, 11):
    data = "{} line.\n".format(i)
    f.write(data)
f.close()
