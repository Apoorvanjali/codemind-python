import math
n=int(input())
s1=0
t=n
s=abs(n)
while s!=0:
    r=s%10
    s1=s1*10+r
    s=s//10
if(n>0):
    print(s1)
else:
    print(-1*s1)