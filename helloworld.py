A=input()
B=A[len(A)-1]
C=len(A[1:len(A)-1])
s=''
for i in range(C):
    s=s+'_'
print(A[0]+s+B)    