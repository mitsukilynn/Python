A=input().split()
S=(int(A[0])*2+int(A[1]))%3
#print(S)
if(S==0):
    print("普通")
elif(S==1):
    print("吉")
elif(S==2):
    print("大吉")
