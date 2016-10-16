# Attempt to solve signzy's coding challenge

import pymysql.cursors
import os.path

connection = pymysql.connect(host='localhost',
	                             user='root',
	                             password='test@1234',
	                             db='signzy',
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)

def loadFilesPushToDb():
	# Reading firstnames.out and lastnames.out and 
	# write all combinations to a file 'fullnames'
	# so as to LOAD INTO MySQL table
	
	if (not os.path.isfile('./fullnames')):
		print "File exists, using it."
		fN = open('firstnames.out')
		lN = open('lastnames.out')
		fullNames = []
		fNames = fN.read().split('\n')
		fNames.sort() # sorting firstname list
		lNames = lN.read().split('\n')
		lNames.sort() # sorting lastnames list
		targetFile = open('fullnames', 'w')
		for fNs in fNames:
			for lNs in lNames:
				targetFile.write(fNs)
				targetFile.write(", ")
				targetFile.write(lNs)
				targetFile.write("\n")
		targetFile.close()

	# Connect to the database
	try: 
		with connection.cursor() as cursor:
			sql = "TRUNCATE TABLE names"
			cursor.execute(sql)
			connection.commit()
			sql = "LOAD DATA INFILE '/Users/adas/Downloads/signzy/pysol/fullnames' INTO TABLE names FIELDS TERMINATED BY ',' (firstname, lastname);"
			cursor.execute(sql)
			connection.commit()
	finally:
		return None

def usernameQuery():
	inputLetters = raw_input("Enter the first three letters: ")
	# Querying DB
	try: 
		with connection.cursor() as cursor:
			# Query DB with letters in firstname column
			print "Finding names based on input (similar to firstname & ordered by FIRSTNAME):"
			sql = "SELECT * FROM names WHERE firstname LIKE '" + inputLetters + "%' ORDER BY firstname LIMIT 5"
			cursor.execute(sql)
			for num in range(0,5):
				result = cursor.fetchone()
				connection.commit()
				if (result is not None):
					print(result['firstname'] + result['lastname'])
				else:
					print "No result in this category."
					break

		print "\n"

		with connection.cursor() as cursor:
			# Query DB with letters in firstname column
			print "Finding names based on input (similar to lastname & ordered by FIRSTNAME):"
			### Ordering this query by firstname too since names are ordered by firstname.
			sql = "SELECT * FROM names WHERE lastname LIKE '%" + inputLetters + "%' ORDER BY firstname LIMIT 5"
			cursor.execute(sql)
			for num in range(0,5):
				result = cursor.fetchone()
				connection.commit()
				if (result is not None):
					print(result['firstname'] + result['lastname'])
				else:
					print "No results in this category."
					break
	

		default = 'Y'
		anotherRound = raw_input("Another query? (Y/n): ") # Default input is 'Y'
		if not anotherRound:
			anotherRound = default
		if (anotherRound == 'Y'):
			usernameQuery()
	finally:
		connection.close()

loadFilesPushToDb()
usernameQuery()