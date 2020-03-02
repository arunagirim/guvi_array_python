l=list(map(int,input().split()))
m=l.pop()
n=l.pop()
a=list(map(int,input().split()))
l=[]
for i in range(n-1):
  if (abs(a[i]-a[i+1]))>m:
    l.append('1')
  else:
    l.append('0')
if abs(a[n-1]-a[0])>m:
  l.append('1')
else:
  l.append('0')
print(" ".join(l))
