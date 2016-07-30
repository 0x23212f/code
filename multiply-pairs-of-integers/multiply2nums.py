f = open('file', 'rU')

c = []
for line in f:
    c = line.split()
    if (len(c) == 2):
        print int(c[0]) * int(c[1])

f.close()
