import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/10986
public class SumOfRemainder {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int seq[] = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            seq[i] = Integer.parseInt(st.nextToken()) % M;
        }

        int prefixSum[] = new int[N];
        prefixSum[0] = seq[0] % M;

        long count[] = new long[M];
        count[prefixSum[0]]++;

        for (int i = 1; i < N; i++) {
            prefixSum[i] = (prefixSum[i - 1] + (seq[i] % M)) % M;
            count[prefixSum[i]]++;
        }

        long answer = 0;
        answer += count[0]; // i==j 인 경우 (나머지가 0)
        for (int i = 0; i < M; i++) {
            long n = count[i];
            if (n > 1) {
                answer += n * (n - 1) / 2; // nC2
            }
        }

        System.out.println(answer);
    }

}
