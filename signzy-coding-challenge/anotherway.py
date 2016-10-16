fN = open('firstnames.out')
lN = open('lastnames.out')
fullNames = []

with open('firstnames.out') as fN, open('lastnames.out') as lN:
    fullNames = []
    fNames = fN.read().split('\n')
    lNames = lN.read().split('\n')

with open('fullnames', 'w') as targetFile:
    for fNs in fNames:
	for lNs in lNames:
	    targetFile.write(fNs + ", " + lNs)