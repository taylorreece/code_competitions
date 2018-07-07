#!/usr/bin/python
import md5

password = ''
c = 0
while len(password) < 8:
	c += 1
	tmp = md5.md5('uqwqemis' + str(c)).hexdigest()
	if tmp[:5] == '00000':
		password += tmp[5]
		print(c, password)
