x,n=map(int,input().split())
passengers=x*100
if n>passengers:
    remaining_passengers=n-passengers
    if remaining_passengers%100==0:
        planes=remaining_passengers//100
    else:
        planes=(remaining_passengers//100)+1
else:
    planes=0
print(planes)
