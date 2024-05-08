import sys 
from collections import deque

M, N = map(int, sys.stdin.readline().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0 
q = deque()

for i in range(N) : 
    temp = list(map(int, sys.stdin.readline().split(' ')))
    graph.append(temp)

for i in range(N) : 
    for j in range(M) : 
        if graph[i][j] == 1 : 
            q.append((i,j))

def bfs() : 
    while q : 
        y,x = q.popleft()
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<M and 0<=ny<N and graph[ny][nx] == 0: 
                graph[ny][nx] = graph[y][x] + 1
                q.append((ny,nx))
            
bfs()

for i in graph : 
    for j in i : 
        # 익지 않은 토마토가 있다면 
        if j == 0 : 
            print(-1)
            exit()
    ans = max(ans, max(i))
# 처음에 0이 아니라 1부터 시작했으니까 
print(ans-1)