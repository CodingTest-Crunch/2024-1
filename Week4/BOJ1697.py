import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split(' '))
dist = [0] * 100001

dx = [-1,1]

# 최단거리 - bfs 예상할 수 있다
def bfs(): 
    q = deque()
    q.append(N)
    
    while q :
        x = q.popleft()
        if x == K : 
            print(dist[x])
            break
        for nx in (x-1,x+1,2*x) : 
            # 0<=nx<K 아닌 이유 - K 넘어가서 -1 해서 K에 올 수도 있음
            if 0<=nx<=100000 and not dist[nx] : 
                dist[nx] = dist[x] + 1
                q.append(nx)
                
    
bfs()

# dp로도 풀기