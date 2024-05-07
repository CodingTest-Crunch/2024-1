import sys
# 최단 거리를 구하는 거니까 일단 초기화는 엄청 큰 값으로!
INF = int(1e9) 

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[INF for i in range(n+1)] for i in range(n+1)]

# 노드 1에서 1로 가는 건 0이니까 초기화하고 시작!
for i in range(1, n+1) : 
    for j in range(1, n+1) : 
        if i == j : 
            arr[i][j] = 0 

# 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있으니 
# min을 사용해서 작은 값을 반영한다 
for i in range(m) : 
    a,b,c,= map(int, sys.stdin.readline().split(" "))
    arr[a][b] = min(c, arr[a][b])

# 플루이드-워셜 돌리기 
for k in range(1,n+1) : 
    for i in range(1,n+1) : 
        for j in range(1,n+1) : 
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

# INF라면 도달할 수 없는 부분이라 값이 업데이트가 안되었으니까 
# 0으로 출력
for i in range(1, n+1) : 
    for j in range(1, n+1) : 
        if arr[i][j] == INF : 
            print(0, end=" ")
        else : 
            print(arr[i][j], end=" ")
    print()