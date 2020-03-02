n=int(input())
a=list(map(int,input().split(" ")))
c=0
for i in a:
  if a.count(i)>1:
    for x in range(a.count(i)):
      a.remove(i)
    c+=1
    print(i,end="")
if c==0:
  print(-1)
