n=int(input())
l=list(map(int,input().split()))
if sum(l)//len(l) in l:
    print("True")
else:
    print("False")