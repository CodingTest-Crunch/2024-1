import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class BOJ_카드_게임_2164 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Deque<Integer> deque = new ArrayDeque<>();
        for(int i = 1; i <= N; i++) {
            deque.add(i);
        }
        int answer = getAnswer_solution(deque);
        System.out.println(answer);
    }

    private static int getAnswer(final Deque<Integer> deque) { // 내가 쓴 답
        while (!deque.isEmpty()) {
            Integer top = deque.pop();
            Integer polled = deque.poll();
            if (polled == null) { // null을 다루는 것을 지양해야하는데..
                return top;
            }
            deque.offer(polled);
        }
        throw new IllegalArgumentException("답이 없어요"); // 이게 걸렸었다.
    }

    private static int getAnswer_solution(final Deque<Integer> deque) { // 다른 사람의 솔루션!
        while (deque.size() > 1) { // 사이즈가 1이 될 때까지만 진행한다.
            deque.poll();
            deque.offer(deque.poll());
        }
        return deque.poll();
    }

}
