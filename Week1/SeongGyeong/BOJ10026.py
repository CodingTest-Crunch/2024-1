import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []
visited = [[0 for i in range(100)] for i in range(100)]

ans = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R = 0 
G = 0 
B = 0 

for i in range(N) : 
    arr = [char for char in sys.stdin.readline().strip()]
    graph.append(arr)

def bfs(graph, visited, x, y) : 
    q = deque()
    q.append((x,y))
    visited[y][x] = 1
    
    while q: 
        x, y = q.popleft()
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N : 
                if graph[ny][nx] == graph[y][x] and visited[ny][nx] == 0 : 
                    q.append((nx,ny))
                    visited[ny][nx] = 1

for i in range(N) : 
    for j in range(N) : 
        if visited[i][j] == 0 : 
            bfs(graph, visited, j, i)
            if graph[i][j] == 'R' : 
                R += 1
            elif graph[i][j] == 'B' :
                B += 1
            else : 
                G += 1

ans.append(R+G+B)

R = 0 
G = 0 
B = 0 
visited = [[0 for i in range(100)] for i in range(100)]

for i in range(N) : 
    for j in range(N) : 
        if graph[i][j] == 'G' :
            graph[i][j] = 'R'                  

for i in range(N) : 
    for j in range(N) : 
        if visited[i][j] == 0 : 
            bfs(graph, visited, j, i)
            if graph[i][j] == 'R' : 
                R += 1
            elif graph[i][j] == 'B' :
                B += 1
                
ans.append(R+B)

print(ans[0], ans[1])

