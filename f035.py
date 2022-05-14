A=input()
s=''
if(50>len(A)):
    for i in A:
        B=str(ord(i))
        s=s+B+'_' #s=s+str(ord(i))+'_'
    print(s[0:len(s)-1])