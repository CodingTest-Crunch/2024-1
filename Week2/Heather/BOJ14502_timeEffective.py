import copy
import sys
from collections import deque
# 조합 지원하는 모듈
from itertools import combinations

N, M= map(int,sys.stdin.readline().split(" "))
graph=[]
for i in range(N):
    arr = list(map(int, sys.stdin.readline().split(' ')))
    graph.append(arr)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus = []
blank = []

answer = 0 

for y in range(N):
    for x in range(M):
        if graph[y][x] == 2:
            virus.append([x, y])
        if graph[y][x] == 0:
            blank.append([x, y])

def bfs() : 
    # 조합 시간 복잡도 - O(2^n)
    for i in combinations(blank, 3) : 
        
        q = deque()
        tmp_graph = copy.deepcopy(graph)
    
        for x,y in i : 
            tmp_graph[y][x] = 1
        
        for i in range(len(virus)):
            q.append(virus[i])
            
        while q : 
            x, y = q.popleft()
            for i in range(4) : 
                nx, ny = x + dx[i], y + dy[i]
                    
                if 0<=nx<M and 0<=ny<N : 
                    if tmp_graph[ny][nx] == 0 : 
                        tmp_graph[ny][nx] = 2
                        q.append([nx, ny])

        global answer 
        cnt = 0
        for i in range(N) :
            cnt += tmp_graph[i].count(0)
        answer = max(cnt, answer)

bfs()
print(answer)