
#?백준2525
A , B = map(int,input().split())
C = int(input())
if B + C >= 60:
    if A == 23:
        A = 0
        B= (B + C)-60
    else:
        A = A+1
        B = (B + C)-60
else:
    B = B + C 
print(A,B)