import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_2841_외계인의기타연주 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        List<PriorityQueue<Integer>> strings = new ArrayList<>();
        for (int i = 0; i < 6; i++) {
            strings.add(new PriorityQueue<>((a, b) -> b - a));
        }
        int count = 0;

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int stringNo = Integer.parseInt(st.nextToken());
            int fretNo = Integer.parseInt(st.nextToken());
            PriorityQueue<Integer> priorityQueue = strings.get(stringNo - 1);
            while (!priorityQueue.isEmpty() && priorityQueue.peek() > fretNo) {
                priorityQueue.poll();
                count++;
            }
            if (!priorityQueue.isEmpty() && priorityQueue.peek() == fretNo) {
                continue;
            }
            priorityQueue.add(fretNo);
            count++;
        }

        System.out.println(count);
    }

}
