#!/usr/bin/python
import re

mystring = '1113222113'

for i in range(40):
	mystring = ''.join([str(len(m.group(0)))+m.group(0)[0] for m in re.finditer(r"(\d)\1*", mystring)])

print len(mystring)
