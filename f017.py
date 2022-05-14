A=input()
s=''
if(35>len(A)):
    for i in A:
        s=s+i+'-'
    print(s[0:len(s)-1])