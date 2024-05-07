
import java.io.*;
import java.util.*;

public class BOJ_10816 {

    public static int n;
    public static int m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        String str1[] = br.readLine().split(" ");
        int a[] = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(str1[i]);
        }
        Arrays.sort(a);

        m = Integer.parseInt(br.readLine());
        String str2[] = br.readLine().split(" ");
        int b[] = new int[m];
        for (int i = 0; i < m; i++) {
            b[i] = Integer.parseInt(str2[i]);
            int lowerBound = lowerBound(a, b[i]);
            int upperBound = upperBound(a, b[i]);
            bw.write((upperBound - lowerBound) + " ");
        }
        bw.flush();
        bw.close();
        br.close();
    }

    public static int lowerBound(int[] arr, int target) {
        int left = 0;
        int right = arr.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    public static int upperBound(int[] arr, int target) {
        int left = 0;
        int right = arr.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}


/* 시간 초과 코드!
public class BOJ_10816 {

    public static int n;
    public static int m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        String str1[] = br.readLine().split(" ");
        int a[] = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(str1[i]);
        }
        Arrays.sort(a);

        m = Integer.parseInt(br.readLine());
        String str2[] = br.readLine().split(" ");
        int b[] = new int[m];
        for (int i = 0; i < m; i++) {
            b[i] = Integer.parseInt(str2[i]);
            bw.write(binarySearch(a, b[i]) + " ");
        }
        bw.flush();
        bw.close();
        br.close();
    }

    public static int binarySearch(int a[], int target) {
        int left = 0;
        int right = n - 1;
        int mid = 0;
        int cnt = 0;
        while (left <= right) {
            mid = (left + right) / 2;
            if (a[mid] < target) {
                left = mid + 1;
            } else if (a[mid] > target) {
                right = mid - 1;
            } else {
                cnt++;
                break;
            }
        }
        if (cnt == 1) {
            for (int i = mid + 1; i < n && a[i] == target; i++) {
                cnt++;
            }
            for (int i = mid - 1; i >= 0 && a[i] == target; i--) {
                cnt++;
            }

        }
        return cnt;
    }
}
 */
