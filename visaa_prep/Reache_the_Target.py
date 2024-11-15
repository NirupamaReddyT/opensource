n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    print(x-y+1 if x-y>=0 else 0)
