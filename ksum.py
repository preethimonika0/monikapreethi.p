N,K=map(int,raw_input().split())
r=list()
for i in range(0,n):
  i=int(raw_input())
  r.append(i)
s=0
for m in range(k):
  s+=r[m]
print s
