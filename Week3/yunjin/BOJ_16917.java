
import java.io.*;
import java.util.*;

public class BOJ_16917 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter((System.out)));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());

        bw.write(Integer.toString(totalCount(a, b, c, x, y)));
        bw.flush();
        bw.close();
        br.close();
    }

    public static int totalCount(int a, int b, int c, int x, int y) {
        int value = Math.min(x, y);
        int ans = 0;
        if (a + b > 2 * c) {
            ans = value * 2 * c;

        } else {
            ans = (a + b) * value;
        }
        //후라이드 더 사야할 경우
        if (value == x) {
            int cnt = y - x;
            ans += Math.min(cnt * 2 * c, cnt * b);

        } else { // 양념 더 사야할 경우
            int cnt = x - y;
            ans += Math.min(cnt * 2 * c, cnt * a); // cnt*2*c : keypoint - 양념에 필요한 후라이드가 필요하지 않아도 최소비용을 위해 추가해준다
        }
        return ans;
    }
}
