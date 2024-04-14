import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class BOJ_11286_절댓값힙 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>((a, b) -> {
            int absA = Math.abs(a);
            int absB = Math.abs(b);

            if (absA == absB) {
                return a - b;
            }
            return absA - absB;
        });

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            int operator = Integer.parseInt(br.readLine());
            if (operator == 0) {
                if (priorityQueue.isEmpty()) {
                    sb.append(0 + "\n");
                    continue;
                }
                sb.append(priorityQueue.poll() + "\n");
                continue;
            }
            priorityQueue.add(operator);
        }

        System.out.println(sb);
    }

}