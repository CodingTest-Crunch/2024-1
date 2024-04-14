## 5. 카드게임

[문제 보기](https://www.acmicpc.net/problem/2164)


### 문제 분석


- input
  - 첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.
- 시간 제한: 2초


### 핵심 아이디어

핵심 아이디어는 큐를 쓰는 것이다. 나가는 방향과 들어오는 방향이 반대로 고정되어있기 때문에 큐를 쓰면 된다. ^_^



### 기록해 둘 이야기 (헷갈렸던 것, 모르겠는 것)

나는 while 조건을 큐가 비어있지 않는 것으로 해두었는데, 코드가 좀 복잡해지는 경향이 있었다.

```java
private static int getAnswer(final Deque<Integer> deque) {
    while (!deque.isEmpty()) {
        Integer top = deque.pop(); // (1)
        Integer polled = deque.poll();
        if (polled == null) { // (2)
            return top;
        }
        deque.offer(polled);
    }
    throw new IllegalArgumentException("답이 없어요"); // (3)
}
```

순서대로 살펴보자.

- (1): 버린 카드인 top을 저장하고 있다.
- (2): 두 가지 개선점이 있다.
  - 마지막에 딱 한번 true가 되는 조건문을 사용하고 있다.
  - null을 직접 다루는 좋지 않은 방식이다.
- (3): 고려해야하는 예외상황이 생긴다. (while 안에서 return 하는 방식이기 때문)

여러모로 개선할 여지가 있었고, 다른 사람의 코드를 찾아보았다.

```java
private static int getAnswer_solution(final Deque<Integer> deque) { // 다른 사람의 솔루션!
    while (deque.size() > 1) { // 사이즈가 1이 될 때까지만 진행한다.
        deque.poll();
        deque.offer(deque.poll());
    }
    return deque.poll();
}
```

아주 깔끔하고 이해하기 쉬운 제어문이 되었다.
그리고 생각보다 훨씬 직관적인 코드였다. 한 장만 남겨두고, 그 한 장을 반환하는 것은 문제를 그대로 옮겨적은 것과 같다.