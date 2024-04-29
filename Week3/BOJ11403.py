import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N) : 
    temp = list(map(int, sys.stdin.readline().split(" ")))
    arr.append(temp)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1
                
for row in arr:
    print(' '.join(map(str, row)))