n, m = list(map(int, input().split()))
A=[]
for i in range(1,n+1):
    A.append(list(map(int, input().split())))
    for j in range(m):
        A[i][j]=A[j][n-i+1]

for i in range(n):
    print(*[A[i][j] for j in range(m)])
