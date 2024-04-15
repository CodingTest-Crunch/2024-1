import java.util.*;

public class BOJ_15681 {
    public static List<Integer> tree[];
    public static boolean check[];
    public static int sum[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int node = sc.nextInt();
        tree = new ArrayList[node + 1];
        check = new boolean[node + 1];
        sum = new int[node + 1];

        for (int i = 1; i < node + 1; i++) {
            tree[i] = new ArrayList<>();
        }
        int root = sc.nextInt();
        int query = sc.nextInt();
        for (int i = 0; i < node - 1; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            tree[a].add(b);
            tree[b].add(a);

        }
        getSum(root);

        for (int i = 0; i < query; i++) {
            int ans = sc.nextInt();
            System.out.println(sum[ans]);

        }
    }

    public static void getSum(int root) {

        check[root] = true;
        sum[root] = 1; // 자기 자신

        for (int i = 0; i < tree[root].size(); i++) {
            int child = tree[root].get(i);
            if (!check[child]) {
                getSum(child);

                // 순서중요
                sum[root] += sum[child];

            }
        }
    }

}