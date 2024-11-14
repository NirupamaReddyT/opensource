N=int(input())
k=int(input())
binary=bin(N)[2:]
if len(binary)>=k and binary[-k]=='1':
    print("true")
else:
    print("false")
