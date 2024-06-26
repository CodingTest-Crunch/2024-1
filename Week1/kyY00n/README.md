# 4월 1주차 알고리즘

4/1 ~ 4/7 까지 푼 문제들입니다. 

## 1. 나머지 합

[문제 보기](https://www.acmicpc.net/problem/10986)

### 문제 분석

- input
  - 1 <= N <= 10^6: 수열의 크기
  - 2 <= M <= 10^3: divisor
  - 0 <= A_i <= 10^9: 수열의 요소
- 시간 제한: 1초

### 핵심 아이디어

- 수열의 크기는 1M 이지만, 부분 수열을 완전탐색으로 찾기 위해서는 100M의 계산을 훌쩍 넘을 것이다. -> 부분합을 이용한다.

- 우리가 궁금한 건, 부분합 자체가 아니라 부분합을 M으로 나눈 값이다.
  - 따라서, prefixSum 배열을 두고 계속해서 M으로 나눠서 저장한다.
  - prefixSum[i] = (prefix[i - 1] + (A[i] % M)) % M
    이 아이디어를 이용한다.
- 1에서 부터의 부분합의 나머지가 같은 i와 j (i <= j)의 부분합 p[i, j]는 prefixSum[j] - prefixSum[i] 이므로, prefixSum[j] 와 prefixSum[i]가 동일한 i와 j를 찾으면 된다. -> 갯수를 미리 세고, 조합(2개를 뽑으면 되니 $$nC2$$ 공식)을 사용한다.

### 내가 계속해서 틀린 이유

이 문제의 아이디어까지 확인하고 확신에 찬 상태로 여러번 제출하면서도 번번이 틀렸다.
알고보니 그 이유는

`count` 배열과 answer 변수의 **자료형** 때문이었다.

이 둘은 부분배열의 가짓수를 저장하는 용도의 변수들이기 때문에, int 범위를 벗어날 수도 있다.

한번 볼까?

언제 count 요소와 answer 의 값이 가장 클까?

바로 수열의 크기가 최대 크기인 10^6이고, A_i가 모두 동일한 때 count 가 가장 크다.
그리고 answer까지 가장 커지려면 A_i가 모두 M의 배수여야한다. (`A_i % M == 0` 인 경우 요소 갯수 만큼 answer가 늘어나기 때문에)

이때, prefixSum 배열은 이런 형태일 것이다.

```java
{ 0, 0, 0, ....., 0 }
```

그렇다면 `count` 배열은 어떻게 될까?

`count[0] = (10 ^ 6) * (10 ^ 6 - 1) / 2 = 499,999,500,000`이 된다.
그러면 int를 벗어난다.

`answer` 는 어떻게 될까?

`answer = (10^6) + (10 ^ 6) * (10 ^ 6 - 1) / 2 = 500,000,500,000` 가 된다. 마찬가지로 int를 벗어난다.

따라서 두 자료형 모두 long 을 사용해주는 것을 반드시 짚고 넘어가자.

## 2. 수들의 합 5

[문제보기](https://www.acmicpc.net/problem/2018)

### 문제 분석

- input
  - N(1 ≤ N ≤ 10,000,000)
- 시간 제한: 2초

### 핵심 아이디어

- 포인터 두 개를 사용한다. (`left`, `right`)
- 합을 구할 때, 매번 전부 다시 계산하지 않고 이동한 포인터에 대해서만 값을 반영해준다.

### 헷갈렸던 것

헷갈렸던 것이, 전부 while 블록과 관련있었다.

```java
while (left <= right) {
    if (sum == N) {
        answer++;
    }
    if (sum < N) {
        right++;
        sum += right;
    } else {
        sum -= left;
        left++;
    }
}
```

1. while 조건
    : do while을 사용하고, 조건을 `left < right` 로 했었다.
    그리고, `answer = 1`로 초기화 했는데, 이 로직에는 반례가 있었다.
    만약 N 이 1일 경우, 일단 do while 블록이 한 번 실행되기 때문에 answer가 1이 되어버리는 것이었다.
2. `right`과 `left` 갱신 순서
   : 구간 자체가 오른쪽으로 이동(left, right 이 1에서 시작)하기 때문에 두 포인터의 이동을 반영할 때 순서를 달리해야했다.
    - `right` 포인터가 이동하면 새로운 숫자를 더해야한다. 즉, 새로운 숫자를 `sum`에 더하기 위해 포인터를 먼저 이동하고 `sum`에 `right` 을 더해주어야 한다.
    - `left` 포인터가 이동하면 기존의 숫자를 빼야한다. 즉, 기존의 숫자를 `sum`에서 빼기 위해, `sum` 에서 `left`를 뺀 뒤에 포인터를 오른쪽으로 이동시켜야한다.

## 3. 먹을 것인가 먹힐 것인가

[문제 보기](https://www.acmicpc.net/problem/7795)

### 문제 분석

- 시간제한: 1초
- 입력
  - 1 ≤ N, M ≤ 20,000

시간복잡도가 $N^2$ 이 나오면 안된다. ($20,000^2*2$ > 1억 이라서..)

과제에서 비슷한 문제를 풀었는데, 정렬을 한 뒤 포인터를 쓰는 것이다.
그리고 정렬된 상태에서 포인터로 중복 계산을 줄여주면 $O(nlogn)$ 이 된다.

### 핵심 아이디어

A, B 를 둘 다 정렬해 준 다음, A와 B 모두 포인터로 순회하면서 답을 찾아간다.

입력, 테스트케이스 반복 로직을 제외하면 다음 메서드만 보면 된다.
참고로, 인자로 들어오는 A와 B는 정렬이 되어있는 상태.

```java
private static void test(int[] A, int[] B) {
    int answer = 0;

    int count = 0; // 포인터, A[i] 보다 작은 B배열 요소 갯수.
    for(int i = 0; i < A.length; i++) { // A에서 작은 것부터
        while(count < B.length) {
            if (B[count] >= A[i]) { // count는 작은 요소 갯수이면서, '다음' 인덱스가 된다.
                break; // count는 다음 인덱스이기 때문에, B[count]가 A[i]랑 같거나 그보다 크면, 멈추는 것이다.
            }
            count++;
        }

        answer += count; // 작은 요소 갯수 더해주기
    }

    System.out.println(answer);
}
```

### 헷갈렸던 것

코드 주석으로도 써놓았지만, 포인터가 좀 헷갈렸었다.
와 방금 변수명을 바꾸었는데 정말 좋은 코드가 된거같다. (변수명의 중요성...)
어쨌든, 미래의 나를 위해 설명해보자면

 A[i] < A[j] 인 경우 A[i]가 먹을 수 있는 물고기는 A[j]도 모두 먹을 수 있다.
그리고 A는 정렬이 되어있다. 그러므로 우리는 B를 돌면서 A[i]가 커짐에 따라, 먹을 수 있는 물고기쌍을 추가해주면 된다. A[i] 물고기가 먹을 수 있는 갯수를 count라고 이름 붙였다.
처음엔 먹을 수 있는게 0마리, 그리고 이 마릿수는 B 배열에서 **다음으로 확인해야하는 인덱스**가 된다.

e.g. 내가 먹을 수 있는 물고기가 B[3] 인것 까지 알고 있다. 그럼 count는 4개 될것. (0, 1, 2, 3) 그럼 내가 다음으로 확인해야하는 건 B[4] (=B[count]) 이다. 

이게 헷갈려가지구.. while 블록에서 헤멨었다.

## 4. 스택 수열

[문제 보기](https://www.acmicpc.net/problem/1874)

### 문제 분석

- 시간 제한: 2초
- 입력 크기
  - n개의 수열
  - 1 ≤ n ≤ 100,000

### 핵심 아이디어

마지막으로 넣은 수를 변수로 저장해두는 것이 아이디어였다.
애초에 스택을 쓰는 건 문제에 주어져서 문제가 없었다.

### 헷갈렸던 것

마지막으로 넣은 수를 어떻게 활용하는지가 헷갈렸었다.

`마지막으로_넣은_수` 이 변수를 1로 초기화해두고, 넣을 때마다 1을 더해주는 것이었다.
while 조건도 조금은 헷갈렸는데, 나는 조건을 `마지막으로_넣은_수 < 이번에_비교할 수` 로 했었기 때문에 컨트롤이 어려웠었다.
그렇게 하지 않고 같은 경우까지 넣어주고 다시 빼는 로직으로 바꾸니 굉장히 간단해졌다.

```java
int 마지막으로_넣은_수 = 1;
for(int i = 0; i < N; i++) {
    int 이번에_비교할_수 = seq[i];
    if (마지막으로_넣은_수 <= 이번에_비교할_수) {
        while(마지막으로_넣은_수 <= 이번에_비교할_수) { // (1) 같은 경우까지 넣어준다.
            stack.push(마지막으로_넣은_수++);
            sb.append("+\n");
        }
        // (2) 만약에 같았어도 다시 빼면 되기 때문이다. 그리고 어차피 출력도 해줘야 함.
        stack.pop();
        sb.append("-\n");
        continue;
    }
    int 스택의_top = stack.pop();
    if (스택의_top > 이번에_비교할_수) { // 비교할 수보다 큰 건 아직 나오면 안되는데!
        System.out.println("NO");
        return;
    }
    sb.append("-\n");
}
```