import sys 
from collections import deque

N = int(sys.stdin.readline())

dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]
graph = []
visited = [[0 for i in range(25)] for i in range(25)]

# for i in range(N) : 
#     num = sys.stdin.readline().strip()
#     arr = []
#     for i in range(len(num)):
#         arr.append(int(num[i]))
#     graph.append(arr)

for i in range(N) : 
    graph.append(list(map(int, sys.stdin.readline().strip())))


def bfs(graph, visited, x,y) : 
    q = deque()
    q.append((x,y))
    visited[y][x] =1
    ans = 1
    
    while q : 
        x, y = q.popleft()
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[ny][nx] == 0 : 
                if graph[ny][nx] == 1:
                    ans += 1
                    q.append((nx,ny))
                    visited[ny][nx] = 1        
    return ans

num = 0 
ans_arr = []
for i in range(N) : 
    for j in range(N) : 
        if visited[j][i] == 0 and graph[j][i] == 1 : 
            ans_arr.append(bfs(graph,visited,i,j))
            num += 1

ans_arr.sort()
print(num)
for i in range(len(ans_arr)):
    print(ans_arr[i])            
    