A=input().split()
B=' '+A[len(A)-1]
s=''
for i in A[0:len(A)-1]:
    s=s+' '+i+' little,'
print(s[0:len(s)]+B+" little Indians")