s=input()
s1=""
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        s1+=s[i-1]+str(count)
        count=1
s1+=s[-1]+str(count)
print(s1)
