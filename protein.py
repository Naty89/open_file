s =[]
with open("/home/naty/Downloads/protein_sequence.txt", "r+")as k:
	p = k.read()
	x = p.split()
	for i in range(len(x)):
		if x[i] not in s:
			s.append(x[i])
		
l = [i for i in s if len(i) == 12]	 

for i in s:
	for k in l:
		if len:
			pass
		else:
			l.append(i)

for i in l:
	print(i + "\t" + )

