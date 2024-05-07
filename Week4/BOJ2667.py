import sys

N = int(sys.stdin.readline())
graph = []

for i in range(N) : 
    temp = list(map(int, sys.stdin.readline().strip()))
    graph.append(temp)

visited = [[False for i in range(N)] for j in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

ans = []

cnt = 0 

def dfs(y, x, graph) : 
    global cnt 
    
    for i in range(4) : 
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[ny][nx] and graph[ny][nx] == 1 : 
            cnt += 1
            visited[ny][nx] = True
            dfs(ny, nx, graph)
        
    
for i in range(N) : 
    for j in range(N) : 
        if graph[i][j] == 1 and not visited[i][j]: 
            cnt += 1
            visited[i][j] = True
            dfs(i, j, graph)
            ans.append(cnt)
            cnt = 0 

ans.sort()

print(len(ans))
for num in ans : 
    print(num)
