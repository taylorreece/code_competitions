#!/usr/bin/python
import md5

starter = 'abc'
starter = 'uqwqemis'

zerotoseven = list(range(8))

password = '________'
c = 0
while '_' in password:
	c += 1
	tmp = md5.md5(starter + str(c)).hexdigest()
	if tmp[:5] == '00000' and tmp[5] in [`x` for x in zerotoseven]:
		loc = int(tmp[5])
		if loc in zerotoseven:
			if password[loc] == '_':
				password = password[0:loc] + tmp[6] + password[loc+1:8]
				print(c,password)	
