import sys 
from collections import deque

N = int(sys.stdin.readline())
map = []
visited = [[0 for i in range(25)] for j in range(25)]
cnt = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N) : 
    arr = [int(x) for x in sys.stdin.readline().strip()]
    map.append(arr)
    
def bfs(map, visited, x, y) : 
    q = deque()
    q.append((x,y))
    visited[y][x] = 1
    ans = 1
    
    while q : 
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N : 
                if map[ny][nx] == 1 and visited[ny][nx] == 0: 
                    q.append((nx,ny))
                    visited[ny][nx] = 1
                    ans += 1
    return ans
    
    
for i in range(N) : 
    for j in range(N) : 
        if map[i][j] == 1 and visited[i][j] == 0: 
            cnt.append(bfs(map, visited, j, i))

print(len(cnt))
cnt.sort()
for num in cnt : 
    print(num)
    
            