f = open('file', 'rU')

letter_presses_dict = {
        'a':1, 'b':2, 'c':3, 'd':1, 'e':2, 'f':3,
        'g':1, 'h':2, 'i':3, 'j':1, 'k':2, 'l':3,
        'm':1, 'n':2, 'o':3, 'p':1, 'q':2, 'r':3, 's':4,
        't':1, 'u':2, 'v':3, 'w':1, 'x':2, 'y':3, 'z':4,
        'space':1
}

line_characters = []
for line in f:
    line_characters = list(line)
    if (len(line_characters) > 2):
    	total_presses = 0
    	for c in line_characters:
    		if (c.isalpha()):
    			p = int(letter_presses_dict[c])
    			total_presses += p
    		elif c.isspace():
    			total_presses += 1

	# -1 because it's couting the return at end of each line
	# as a space character, which it is, tbh. lol.
	print total_presses - 1 