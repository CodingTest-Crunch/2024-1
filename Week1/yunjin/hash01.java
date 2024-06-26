import java.util.*;

class hash01 {
    static int nums[];

    // HashSet 이란 중복요소를 허용하지 않음.
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        nums = new int[n];
        for (int i = 0; i < nums.length; i++) {
            nums[i] = sc.nextInt();
        }
        int ans = solution1(nums);
        System.out.println(ans);
    }

    public static int solution1(int[] nums) {
        HashSet<Integer> hs = new HashSet<>();
        for (int num : nums) {
            hs.add(num);
        }
        return Math.min(hs.size(), nums.length / 2);
    }

    public int solution(int[] nums) {
        int max = nums.length / 2;
        HashSet<Integer> hs = new HashSet<>();
        for (int num : nums) {
            hs.add(num);
        }
        int cmp = hs.size();
        if (max >= cmp) {
            return cmp;
        } else {
            return max;
        }
    }
}