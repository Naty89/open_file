with open("words", "r+")as k:
	p=k.read()	
	x=p.split()
	m=[len(j) for j in x]
	y = [i for i in x  if len(i) >= max(m)]
	print(y)
	
