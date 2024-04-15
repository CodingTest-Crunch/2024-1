import java.util.*;

public class BOJ_11725 {
    public static List<Integer> tree[];
    public static boolean check[];
    public static int parent[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int node = sc.nextInt();
        tree = new ArrayList[node + 1];
        for (int i = 0; i < node + 1; i++) {
            tree[i] = new ArrayList<>();
        }
        check = new boolean[node + 1];
        parent = new int[node + 1];

        for (int i = 0; i < node - 1; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            tree[a].add(b);
            tree[b].add(a);
        }
        find(1);
        for (int i = 2; i < node + 1; i++) {
            System.out.println(parent[i]);
        }
    }

    public static void find(int node) {
        check[node] = true;
        for (int i = 0; i < tree[node].size(); i++) {
            int child = tree[node].get(i);
            if (!check[child]) {
                parent[child] = node;
                find(child);
            }
        }
    }
}