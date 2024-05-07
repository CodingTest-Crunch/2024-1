
import java.io.*;

public class BOJ_16922 {

    public static int n, cnt = 0;
    public static int arr[] = {1, 5, 10, 50};
    public static boolean visited[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        visited = new boolean[1001]; // 20*50+1
        n = Integer.parseInt(br.readLine());
        dfs(0, 0, 0);
        bw.write(Integer.toString(cnt));
        bw.flush();
        bw.close();
        br.close();
    }

    public static void dfs(int idx, int sum, int depth) {
        if (depth == n) {
            if (!visited[sum]) {
                cnt++;
                visited[sum] = true;
            }
            return;
        }
        //   1 5 10 50
        for (int i = idx; i < 4; i++) { // 1+1 같은 값을 더하는 것부터 시작하기! 이때 i가 idx부터 시작하도록해서 
            // 1 5 10 50 에서 1 5 // 1 10 // 1 50 // 5 10 // 5 50 // 10 50 이렇게 인덱스가 증가하는 순으로만 보기!
            dfs(i, sum + arr[i], depth + 1);
        }
    }
}
