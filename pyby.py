import sys

if len(sys.argv) != 3:
	sys.exit("Error, invalid number of arguments")

#Since we cant do int comparisons on strings stop program if not given
#an int
try:
	count = int(sys.argv[2])
except ValueError:
	sys.exit("Error: Second value not a number")



if count > 10:
	sys.exit("Count must be less than 10")

if sys.argv[1] == "left":
	for x in range(0, count):
		print "<(-_-<)"	

elif sys.argv[1] == "right":
	for x in range(0, count):
		print "(>-_-)>"
	

elif sys.argv[1] == "dance":
	lBool = False
	for x in range(0, count):
		if (lBool):
			print "(>-_-)>"
			lBool = False
		else:
			print "<(-_-<)"
			lBool = True
		if x == count - 1:
			print "<(0_0)>"

else:
	print "Incorrect value 'left' 'right' 'dance'"
