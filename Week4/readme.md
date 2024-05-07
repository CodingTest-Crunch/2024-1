### 240507

1. 백준 2667 (실버 1, dfs)

   - 최소 경로를 구하는 문제는 아니라서 사실 bfs, dfs 모두 가능한 문제입니다
     - bfs로 너비 우선으로 탐색을 하든, dfs로 깊이 우선 탐색을 하든 한 덩어리 내의 모든 노드를 순회하니까!
   - bfs 풀이만 많이 하다가 dfs를 까먹은 것 같아서 dfs 방법으로 풀이해줬어요

   ```python
   def dfs(y, x, graph) :
   global cnt

   for i in range(4) :
       nx, ny = x + dx[i], y + dy[i]
       if 0<=nx<N and 0<=ny<N and not visited[ny][nx] and graph[ny][nx] == 1 :
           cnt += 1
           visited[ny][nx] = True
           dfs(ny, nx, graph)
   ```
