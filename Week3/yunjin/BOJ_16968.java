
import java.io.*;

public class BOJ_16968 {

    public static String n;
    public static char a[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = br.readLine();
        a = new char[n.length()];
        for (int i = 0; i < a.length; i++) {
            a[i] = n.charAt(i);
        }
        bw.write(Integer.toString(totalCount(a)));
        bw.flush();
        bw.close();
        br.close();
    }

    public static int totalCount(char a[]) {
        int answer = 1;
        if (a[0] == 'c') {
            answer *= 26;
        } else {
            answer *= 10;
        }

        for (int i = 1; i < a.length; i++) {

            if (a[i - 1] == a[i] && a[i] == 'c') {
                answer *= 25;
            } else if (a[i - 1] != a[i] && a[i] == 'c') {
                answer *= 26;
            } else if (a[i - 1] == a[i] && a[i] == 'd') {
                answer *= 9;
            } else if (a[i - 1] != a[i] && a[i] == 'd') {
                answer *= 10;
            }
        }
        return answer;

    }
}
