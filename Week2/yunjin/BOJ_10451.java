import java.util.*;

public class BOJ_10451 {
    public static int child[];
    public static boolean check[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int cnt = sc.nextInt();
        for (int i = 0; i < cnt; i++) {
            int ans = 0;
            int node = sc.nextInt();
            child = new int[node + 1];
            check = new boolean[node + 1];

            for (int idx = 1; idx <= node; idx++) {
                child[idx] = sc.nextInt();
            }
            for (int j = 1; j <= node; j++) {
                if (!check[j]) {
                    find(j);
                    ans++;
                }
            }
            System.out.println(ans);
        }

    }

    public static void find(int node) {
        check[node] = true;
        if (!check[child[node]]) {
            find(child[node]);
        }
    }

}