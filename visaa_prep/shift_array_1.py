n=int(input())
arr=list(map(int,input().split()))
k=arr[0]
a=[]
for i in range(1,n):
    a.append(arr[i])
a.append(k)
print(*a)
