### 240430

1. 백준 11403 (실버 1, 플로이드-워셜)

   - 플로이드 워셜이라는 알고리즘이 있는지 아예 몰랐아요 그래서 그냥 구글링해서 코드 보고 공부했습니다.

   ### 플로이드 워셜

   - 다익스트라가 하나의 정점에서 다른 모든 정점까지의 최단 거리를 구하는 알고리즘이었다면, 플로이드-워셜은 모든 노드 간 최단 경로를 구하는 알고리즘
   - 모든 노드 간의 최단 거리를 구해야하기 때문에 2차원 인접 행렬을 구성한다.
   - 각 라운드마다 각 경로에서 새로운 중간 노드로 활용할 수 있는 노드를 선택하고 더 짧은 길이를 선택하여 줄이는 과정을 반복한다

   ```python
   for k in range(1,n) :
       for i in range(1,n) :
           for j in range(1,n) :
               dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
   ```

### 240502

4. 백준 14500 (골드 4, 구현/dfs)

   - 문제는 이해했고, 그래프 탐색을 이용해야겠다는 생각은 했는데 그 이상 생각이 발전하지 못했어요
   - 한붓그리기로 가능한 모양의 경우에는 dfs로 체크를 해주면 되는데, 한붓그리기가 되지 않고 ㅓ,ㅗ,ㅏ,ㅜ 같은 모양은 따로 체크를 해줬어야 하는데 여기가 좀 까다로웠어요

   ```python
    def exception(y,x):
    global maxValue
    arr = []
    # 일단 네 방향 모두 계산을 한다
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
   ```

   - dfs도 문제를 푼지 오래되고 bfs 위주로 풀어서 까먹었었는데 이 문제로 연습했습니다 :D
