x=int(input())
dis1=x-(x//10)
dis2=x-100
print(dis1 if dis1<dis2 else dis2)
