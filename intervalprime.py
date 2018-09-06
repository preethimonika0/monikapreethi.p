n,q=map(int,raw_input().split())
for i in range(n+1,q):
	if(i>1):
		for m in range(2,i):
			if(i%m==0):
				break
		else:
			print i,
