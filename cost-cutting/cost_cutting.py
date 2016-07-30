f = open('file', 'rU')

c = []
for line in f:
    c = line.split()
    if (len(c) == 3):
        c.sort()
        print c[1]
