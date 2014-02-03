import os
import re

r = open("tags.txt", 'r+')
dogs = ""
line = r.readline()
for line in r:
	dogs += str(line)
	

cats = []

cats.append(re.findall(r"[\w']+", dogs))
geese = []
for i in cats:
	for y in i:
		geese.append("<keyword>" + str(y) + "</keyword>")


for i in list(set(geese)):
	print i






"""

y = []



for i in dogs:
	
	y.append(i.split(" ")
	

for string in y:
	for d in string:
		print "<keyword>" + str(d) + "</keyword>"
	
"""

"""cats = ""
for i in dogs:
	cats += str(i)
mouse = []	
cats.split(' ')
print cats
for i in cats:
	print i
	"""