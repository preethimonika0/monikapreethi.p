n1=int(raw_input())
n2=int(raw_input())
n3=int(raw_input())
if ((n1>n2) and (n1>n3)):
	largest=n1
elif ((n2>n1) and (n2>n3)):
	largest=n2
else:
	largest=n3
print "largest"
