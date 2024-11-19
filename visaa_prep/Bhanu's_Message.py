n=input()
if (n[0]=='+' and n[1:3].isdigit() and n[3]==' ' and len(n)==14 and n[4:].isdigit() and sum(int(d)for d in n[4:])>0):
    print('Correct')
else:
    print('Incorrect')
