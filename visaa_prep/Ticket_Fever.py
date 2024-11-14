n=int(input())
for i in range(n):
    n,m=map(int,input().split())
    diff=n-m
    print(diff if diff>0 else 0)
