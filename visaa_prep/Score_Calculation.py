n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    testcases=x//10
    marks=testcases*y
    print(marks)
