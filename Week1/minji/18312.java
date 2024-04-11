import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int cnt = 0;

        for (int h = 0; h <= N; h++) {
            for (int m = 0; m <= 59; m++) {
                for (int s = 0; s <= 59; s++) {
                    String tmp = String.format("%02d", h) + String.format("%02d", m) + String.format("%02d", s);
                    if (tmp.indexOf(String.valueOf(K)) != -1)  //K가 포함되면
                      cnt++;
                }
            }
        }

        System.out.println(cnt);
    }
}
