### 2024.04.08

1. 백준 1074 (실버 1)

   - 항상 어려워하는 유형인 재귀라서 많이 헤맸습니다...
   - 결국 답지 보고 공부했는데

   ```
       solution(x,y,temp)
       solution(x, y+temp, temp)
       solution(x+temp, y, temp)
       solution(x+temp, y+temp, temp)
   ```

   이 부분을 이해하기가 힘들었어요
   우측으로 움직이는데 왜 y+temp이지? 했는데
   r행 c열이고, `x==r and y==c`로 조건을 잡았기 때문에 우측으로 움직이는 건 열을 이동하는 거고 y를 이동하는 게 맞다!
   좌표 개념보다는 배열 개념으로 생각하는 게 맞는 것 같아요 :D

---

### 2024.04.09

2. 백준 1541 (실버 2)

   - 진짜 지x생쇼를 했습니다,,, (BOJ_1stTry에 그 기록이 있어요)
   - 다 지우고 다시 생각해보니 split으로 엄청 쉽게 풀 수 있었습니다,,,,,허무티비

---

### 2024.04.11

3. 백준 2630 (실버 2)
   - 딱 보자마자 월요일에 풀었던 1074번이랑 같은 유형인 것을 직감하고 재귀로 문제 풀이를 했습니다!
   - 이 문제의 경우에는 0인 경우, 1인 경우를 모두 구해야해서 처음에는 서로 다른 2개의 함수로 만들었다가 로직이 아예 같아서 num 매개변수를 추가하고 하나의 함수로 합쳤습니다!
   - break를 걸어주고 바로 거기서 재귀를 돌려야하는데 어떻게 할까 고민하다가 flag를 추가해줬습니다!
   - 풀이를 찾아보니까
   ```python
   def solution(x, y, N) :
      color = paper[x][y]
         for i in range(x, x+N) :
            for j in range(y, y+N) :
               if color != paper[i][j] :
                  solution(x, y, N//2)
                  solution(x, y+N//2, N//2)
                  solution(x+N//2, y, N//2)
                  solution(x+N//2, y+N//2, N//2)
                  return
      if color == 0 :
         result.append(0)
      else :
         result.append(1)
   ```
   이런 식으로 함수를 한 번만 돌려도 되는 방법이 있어서 해당 방법도 공부했습니다!