import sys

N = int(sys.stdin.readline())
graph = []

for i in range(N) : 
    arr = list(map(int, sys.stdin.readline().split(" ")))
    graph.append(arr)

def solution(x, y, n, num) :
    flag = 0 
    global cnt
    if not (0<=x<x+n and 0<=y<y+n) : 
        return 
    
    for i in range(y, y+n) : 
        for j in range(x, x+n) :
            if graph[j][i] != num : 
                flag = 1
                break
    
    if flag == 1: 
        temp = n //2
        solution(x, y, temp, num)
        solution(x, y + temp, temp, num)
        solution(x+ temp, y, temp, num)
        solution(x+ temp, y + temp, temp,num)
    else : 
        cnt += 1
        return 

cnt = 0 
solution(0,0,N,0)
print(cnt)

cnt = 0  
solution(0,0,N,1)
print(cnt)

