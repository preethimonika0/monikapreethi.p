n=int(raw_input())
temp=n
p=0
while(n!=0):
	r=n%10
	p=p*10+r
	n/=10
if(temp==p):
	print "yes"
else:
	print "no"
