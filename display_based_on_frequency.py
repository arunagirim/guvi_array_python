import collections
n=int(input())
l=list(map(int,input().split()))
cnt=dict(collections.Counter(l))
c=sorted(cnt.items(),key=lambda x: x[1])
while(True):
	for i in range(len(c)-1):
		x=0
		if c[i][1]==c[i+1][1] and c[i][0]>c[i+1][0]:
			c[i],c[i+1]=c[i+1],c[i]
			x+=1
	if x==0:
		break;
r=map(str,[x[0] for x in c])
print(" ".join(r))
