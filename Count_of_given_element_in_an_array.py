n=int(input())
l=list(map(int,input().split()))
m=int(input())
c=0
for i in range(0,len(l)):
    if m==l[i]:
        c+=1
print(c)