with open("words", "r+")as k:
	p=k.read()	
	x=p.split()
	longest = []
	for i in range(len(x)):
		longest.append(len(x[i]))
#	for m in range(len(x)):
		if len(x[m]) == max(longest):
			o = x[m]
			print(o)
k.close()



		


