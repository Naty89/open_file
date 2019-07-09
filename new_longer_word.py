j = []
o = []
from random import choice
for i in range(97, 123):
	j.append(chr(i))
	
with open("words", "r+") as k:
	p=k.read
	x=p.split()
	m = [len(o) for j in x]
	for a in range(max(m)+1):
		o.append(choice(j))
	e = "".join(o)
	k.write(e)
			
