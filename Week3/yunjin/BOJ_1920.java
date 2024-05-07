
import java.util.*;

public class BOJ_1920 {

    public static int n;
    public static int m;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a[] = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        int b[] = new int[m];
        for (int i = 0; i < n; i++) {
            b[i] = sc.nextInt();
            System.out.print(binarySearch(a, b[i]) + " ");
        }
    }

    public static int binarySearch(int a[], int target) {//이분탐색
        Arrays.sort(a);
        int left = 0;
        int right = n - 1;
        int mid;

        while ((left <= right)) {
            mid = (left + right) / 2;
            if (a[mid] < target) {
                left = mid + 1; 
            }else if (a[mid] > target) {
                right = mid - 1; 
            }else {
                return 1;
            }
        }
        return 0;
    }

}
