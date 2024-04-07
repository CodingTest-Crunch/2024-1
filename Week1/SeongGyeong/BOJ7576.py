import sys 
from collections import deque

ox, oy = map(int, sys.stdin.readline().split(' '))
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

for i in range(oy) : 
    arr = list(map(int, sys.stdin.readline().split(' ')))
    graph. append(arr)


# 익은 토마토의 위치 queue에 추가
q = deque()
for i in range(oy):
    for j in range(ox):
        if graph[i][j] == 1:
            q.append((j,i))

def bfs() : 
    while q : 
        x, y = q.popleft()
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<ox and 0<=ny<oy and graph[ny][nx] == 0 : 
                    graph[ny][nx] = graph[y][x] + 1
                    q.append((nx,ny))

res = 0 
bfs()

for i in range(oy) :
    for j in range(ox) : 
        if graph[i][j] == 0 : 
            print(-1)
            exit()
             
print(max(max(graph))-1)
