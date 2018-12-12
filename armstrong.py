n=int(raw_input())
s=0
t=n
while t>0:
	d=t%10
	s+=d**3
	t//=10
	if n==s:
		print("yes")
		break
	else:
		print("no")
		break
