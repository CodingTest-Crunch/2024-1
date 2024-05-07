import sys 
from collections import deque

ox, oy = map(int, sys.stdin.readline().split(' '))
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(oy) : 
        arr = list(map(int, sys.stdin.readline().split(' ')))
        graph.append(arr)
        
q = deque()
for i in range(oy) : 
    for j in range(ox) : 
        if graph[i][j] == 1 : 
            q.append((j,i))

while q : 
    x, y = q.popleft()
    for i in range(4) : 
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<ox and 0<=ny<oy and graph[ny][nx] == 0 : 
            graph[ny][nx] = graph[y][x] + 1
            q.append((nx,ny))

res = 0
for i in range(oy) : 
    for j in range(ox) : 
        if graph[i][j] == 0 : 
            print(-1)
            exit()
    res = max(res, max(graph[i]))
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(res - 1)

# 이렇게 하면 각 행의 첫번쨰 요소만 보고 비교하기 때문에 위처럼 해야한다!
# print(max(max(graph))-1)