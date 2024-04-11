import java.io.BufferedReader;
import java.io.InputStreamReader;

// https://www.acmicpc.net/problem/2018
public class SumOfNumbers {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int answer = 0;
        int left = 1, right = 1;
        int sum = 1;
        while (left <= right) {
            if (sum == N) {
                answer++;
            }
            if (sum < N) {
                right++;
                sum += right;
            } else {
                sum -= left;
                left++;
            }
        }

        System.out.println(answer);
    }

}
