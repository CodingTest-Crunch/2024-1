import sys 
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split(' '))
graph = []
for i in range(N) : 
    arr = list(map(int, sys.stdin.readline().split(' ')))
    graph.append(arr)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0 

# 바이러스 퍼트리기
def bfs() : 
    q = deque()
    tmp_graph = copy.deepcopy(graph)
    
    # 최대 O(n^2)
    for i in range(N) : 
        for j in range(M) : 
            if tmp_graph[i][j] == 2 : 
                q.append((j,i))
    
    while q : 
        x, y = q.popleft()
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
                
            if 0<=nx<M and 0<=ny<N : 
                if tmp_graph[ny][nx] == 0 : 
                    tmp_graph[ny][nx] = 2
                    q.append((nx, ny))
    
    global answer 
    cnt = 0
    for i in range(N) :
        cnt += tmp_graph[i].count(0)
    answer = max(cnt, answer)

# 벽(1) 3개 쌓기
# 백트래킹


# 재귀 - O(2^n)
def makeWall(cnt) : 
    if cnt == 3 : 
        bfs()
        return 
    
    for i in range(N) : 
        for j in range(M) : 
            if graph[i][j] == 0 : 
                # 벽을 세움
                graph[i][j] =1 
                makeWall(cnt+1)
                # 다시 벽을 허뭄 - 백트래킹
                graph[i][j] = 0 

makeWall(0)
print(answer)