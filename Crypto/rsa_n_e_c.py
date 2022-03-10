N=263760064354121
E=13
C=247329055294598
P=0
for i in range(3,N,2):
    if N % i == 0:
        P=i
        break
Q=N//P
R=(P-1)*(Q-1)
D=pow(E,-1,R)
X=pow(C,D,N)
print("Message:",bytearray .fromhex( format(X,'X')).decode())
