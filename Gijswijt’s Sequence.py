s=['1','1'];print("1\n1")
for h in range(998):
	p=0
	for i in range (1,int(len(s)/2)+1):
		a=0
		for j in range (0,len(s),len(''.join(s[len(s)-i:len(s)]))):
			if ''.join(s[len(s)-i-j:len(s)-j]) == ''.join(s[len(s)-i:len(s)]):a=a+1
			else:break
		if (a>p):p=a
	s.append(str(p));print(str(p))
