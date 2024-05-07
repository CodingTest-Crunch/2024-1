import sys 

N,M = map(int, sys.stdin.readline().split())
tetris = []

for i in range(N) : 
    arr = list(map(int, sys.stdin.readline().split()))
    tetris.append(arr)
maxValue = 0 
cnt = 0 

dx = [1,0,-1,0]
dy = [0,-1,0,1]
visited =[[False for i in range(M)] for j in range(N)] 

# dfs - 최소 경로가 아니라 연결된 쌍을 찾아야하니까
# 처음에 자꾸 답이 틀리게 나왔던 이유 
# - dsum을 global 변수로 사용했더니 값이 매 단계마다 제대로 초기화가 안됨
# 매개변수로 사용해서 해결!
def solution(y,x, dsum, cnt) : 
    global maxValue
    if cnt == 4 : 
        if dsum > maxValue : 
            maxValue = dsum  
        return 
   
    for i in range(4) : 
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<M and 0<=ny<N and visited[ny][nx] == False:
            visited[ny][nx] = True
            solution(ny,nx,dsum+tetris[ny][nx], cnt+1)
            visited[ny][nx] = False

# ㅓ,ㅗ,ㅏ,ㅜ - dfs로 안됨 (한붓그리기가 가능하면 dfs)

def exception(y,x): 
    global maxValue
    arr = []
    for i in range(4) : 
        nx,ny = x + dx[i], y+dy[i]
        if 0<=nx<M and 0<=ny<N : 
            arr.append(tetris[ny][nx])
    # 네 방향 모두 범위 안에 들어오면
    if len(arr) == 4 : 
        # 오름차순으로 정렬해서 
        arr.sort(reverse=True)
        # 제일 작은 수 삭제 
        # remove 쓰면 - remove(3) : 배열에서 가장 첫번째로 나오는 3 삭제
        arr.pop(0)
        maxValue = max(maxValue, sum(arr)+tetris[y][x])
    elif len(arr) == 3 : 
        maxValue = max(maxValue, sum(arr)+tetris[y][x])
    return
        
for i in range(N) : 
    for j in range(M) : 
        visited[i][j] = True
        solution(i,j,tetris[i][j],1)
        visited[i][j] = False

        exception(i,j)

print(maxValue)  


